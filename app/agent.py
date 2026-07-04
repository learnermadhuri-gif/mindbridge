"""MindBridge: a cognitive accessibility concierge for neurodivergent users."""

import datetime
import os
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Prefer a simple API key for local demos; fall back to Vertex AI ADC.
api_key = os.getenv("GOOGLE_API_KEY", "")
if api_key:
    os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "False")
else:
    os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    if not project_id:
        try:
            import google.auth

            _, project_id = google.auth.default()
        except Exception:
            project_id = "mindbridge-dev"
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
    os.environ.setdefault(
        "GOOGLE_CLOUD_LOCATION", os.getenv("GOOGLE_CLOUD_LOCATION", "global")
    )


def get_current_time(query: str) -> str:
    """Return the current time for a city or timezone."""
    lower = query.lower()
    if any(tok in lower for tok in ("sf", "san francisco", "los angeles", "la")):
        tz_identifier = "America/Los_Angeles"
    elif any(tok in lower for tok in ("nyc", "new york", "eastern", "et")):
        tz_identifier = "America/New_York"
    elif any(tok in lower for tok in ("london", "gmt", "bst")):
        tz_identifier = "Europe/London"
    else:
        return f"Current local time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time in {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


def break_down_task(task: str, energy_level: int = 5, profile: str = "adhd") -> str:
    """Break a task into small micro-steps matched to energy and neurodivergent profile."""
    steps = []
    if "clean" in task.lower() or "apartment" in task.lower() or "room" in task.lower():
        steps = [
            "1. Stand up and take 3 slow breaths.",
            "2. Pick one small zone (e.g., one corner, one shelf).",
            "3. Grab a trash bag and a laundry basket.",
            "4. Set a 10-minute timer.",
            "5. Put only visible trash into the bag.",
            "6. Put clothes in the basket.",
            "7. Take a 5-minute break.",
            "8. Repeat with the next zone if you have energy.",
            "9. Reward yourself when the timer ends.",
        ]
    elif "email" in task.lower() or "message" in task.lower():
        steps = [
            "1. Open the draft and write the recipient name.",
            "2. Write one sentence: what you need.",
            "3. Write one sentence: why it matters (optional).",
            "4. Add a polite closing.",
            "5. Read it once, then send.",
            "6. Close the app and take a break.",
        ]
    elif "work" in task.lower() or "project" in task.lower():
        steps = [
            "1. Gather all materials in one place.",
            "2. Pick the single smallest next action.",
            "3. Set a timer for 15 minutes.",
            "4. Work only until the timer rings.",
            "5. Note where you stopped.",
            "6. Decide if you want another round.",
        ]
    else:
        steps = [
            "1. Name the task out loud.",
            "2. Identify the very first physical action.",
            "3. Set a timer for 10 minutes.",
            "4. Do only that action.",
            "5. Pause and check in with your body.",
            "6. Continue or stop based on your energy.",
        ]

    if energy_level <= 3:
        steps = [
            *steps[:3],
            "Rest step: lie down, drink water, or stretch before continuing.",
        ]
    elif energy_level <= 6:
        steps = steps[:5]
    else:
        steps.append("Optional: add a small extra step if you still have momentum.")

    profile_hint = {
        "adhd": "Tip: body-doubling (virtual or in-person) can help you start.",
        "autism": "Tip: keep the environment predictable and reduce sensory input.",
        "anxiety": "Tip: focus on one step at a time; you can stop anytime.",
        "general": "Tip: start small and build momentum.",
    }.get(profile.lower(), "Tip: start small and build momentum.")

    return "\n".join(steps) + f"\n\n{profile_hint}"


def suggest_sensory_friendly_plan(
    activity: str, triggers: str, location: str = ""
) -> str:
    """Suggest a low-stimulation plan for an outing based on sensory triggers."""
    triggers_lower = triggers.lower()
    tips = []
    if "noise" in triggers_lower or "sound" in triggers_lower:
        tips.append("- Bring noise-canceling headphones or earplugs.")
    if "crowd" in triggers_lower or "people" in triggers_lower:
        tips.append("- Go during off-peak hours: weekday mornings or early afternoons.")
    if "bright" in triggers_lower or "light" in triggers_lower:
        tips.append("- Wear sunglasses or a brimmed hat indoors if helpful.")
    if "touch" in triggers_lower or "texture" in triggers_lower:
        tips.append("- Wear comfortable, familiar clothing; avoid new fabrics.")
    if "smell" in triggers_lower:
        tips.append("- Bring a small scent buffer (tissue with a familiar scent).")
    if not tips:
        tips.append("- Identify your top trigger and plan one coping tool for it.")

    plan = [
        f"Plan for: {activity}",
        f"Location context: {location or 'your local area'}",
        "",
        "Low-stimulation strategy:",
        *tips,
        "- Pre-game: eat a snack, hydrate, and plan an exit route.",
        "- During: take bathroom breaks to reset even if you don't need one.",
        "- After: schedule quiet recovery time.",
        "",
        "Suggested time: Tuesday-Thursday, 10am-2pm (usually quieter).",
    ]
    return "\n".join(plan)


def draft_message(
    recipient: str, intent: str, tone: str = "gentle-assertive", context: str = ""
) -> str:
    """Draft a message in a chosen tone for a difficult conversation."""
    intent_clean = intent.strip()
    context_clean = context.strip() if context else ""

    tone_body = {
        "gentle-assertive": f"I wanted to share that {intent_clean}.",
        "direct": f"{intent_clean}.",
        "apologetic": f"I'm sorry to ask, but {intent_clean}.",
        "warm": f"Hey, I wanted to share that {intent_clean}.",
    }
    body = tone_body.get(tone.lower(), tone_body["gentle-assertive"])
    if context_clean:
        body = f"{body} {context_clean}"

    tone_closer = {
        "gentle-assertive": "Thanks for your understanding",
        "direct": "Please let me know by [date/time]",
        "apologetic": "I appreciate your patience",
        "warm": "Talk soon",
    }
    closer = tone_closer.get(tone.lower(), tone_closer["gentle-assertive"])

    draft = f"Hi {recipient},\n\n{body}\n\n{closer},\n[Your name]"
    return f"Draft ({tone}):\n\n{draft}\n\nYou can adjust the tone, add specifics, or ask me to make it shorter."


def track_energy(available_spoons: int, tasks: str) -> str:
    """Prioritize tasks based on remaining energy/spoons."""
    task_list = [t.strip() for t in tasks.split(",") if t.strip()]
    if not task_list:
        return "Please share a few tasks and I'll help you prioritize them."

    if available_spoons >= 7:
        priority = "You have solid energy. Try one medium task, then reassess."
        order = task_list[:3]
    elif available_spoons >= 4:
        priority = "You have moderate energy. Pick the smallest must-do task first."
        order = sorted(task_list, key=lambda t: len(t))[:3]
    else:
        priority = "You are running low. Rest is the best choice; if you must do something, pick the one smallest task."
        order = [min(task_list, key=len)] if task_list else []

    output = [
        f"Energy check: {available_spoons}/10 spoons.",
        f"Guidance: {priority}",
        "",
        "Suggested order:",
    ]
    for i, task in enumerate(order, 1):
        output.append(f"{i}. {task}")
    if available_spoons < 4:
        output.append("If you do this one task, stop immediately after and rest.")
    output.append("\nRemember: stopping is also a valid choice.")
    return "\n".join(output)


SAFETY_PREAMBLE = """You are a supportive cognitive accessibility assistant.
NEVER diagnose conditions, prescribe treatments, or give medical advice.
If the user mentions self-harm, suicidal thoughts, or crisis, immediately respond with
empathy, encourage them to contact a crisis line or emergency services, and do not try to solve the task.
Keep responses validating, non-judgmental, and easy to read.
"""

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are MindBridge, a warm, validating concierge for neurodivergent users.\n\n"
        "When the user greets you or asks what you can do, introduce yourself briefly and list the four things you can help with:\n"
        "1) breaking down overwhelming tasks, 2) planning sensory-friendly outings, 3) drafting difficult messages, and 4) tracking energy/spoons.\n\n"
        "Your job is to understand what the user needs and route to the right tool:\n"
        "- If they feel overwhelmed by a task, use `break_down_task`. Ask for the task, and optionally their energy level (1-10) and profile (adhd, autism, anxiety, sensory, general).\n"
        "- If they need to plan an outing or activity with sensory concerns, use `suggest_sensory_friendly_plan`. Ask for triggers if not provided.\n"
        "- If they want help writing a message, use `draft_message`. Ask for recipient, intent, and desired tone.\n"
        "- If they mention energy or 'spoons', use `track_energy`.\n"
        "- For time-aware scheduling, use `get_current_time`.\n\n"
        "Always be warm, validating, and concise. Ask clarifying questions if a profile or energy level is not stated.\n\n"
        "When you use a tool, present its result in a supportive way. Do not contradict the tool's guidance.\n\n"
        f"{SAFETY_PREAMBLE}"
    ),
    tools=[
        get_current_time,
        break_down_task,
        suggest_sensory_friendly_plan,
        draft_message,
        track_energy,
    ],
)

task_breakdown_agent = Agent(
    name="task_breakdown_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "You are a task-breakdown specialist for neurodivergent users.\n"
        "When a user is overwhelmed by a task, use `break_down_task` and then explain the steps in a gentle, validating way.\n"
        "Suggest a timer, a reward, and a body-doubling option when appropriate.\n\n"
        f"{SAFETY_PREAMBLE}"
    ),
    tools=[break_down_task, get_current_time],
)

sensory_planner_agent = Agent(
    name="sensory_planner_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "You are a sensory-friendly planning specialist.\n"
        "Help users plan outings and activities that minimize sensory overload.\n"
        "Use `suggest_sensory_friendly_plan` and ask about triggers if not provided.\n"
        "Always include an exit strategy and recovery time.\n\n"
        f"{SAFETY_PREAMBLE}"
    ),
    tools=[suggest_sensory_friendly_plan, get_current_time],
)

communication_coach_agent = Agent(
    name="communication_coach_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "You are a communication coach for neurodivergent users.\n"
        "Draft messages that are clear, respectful, and match the user's desired tone.\n"
        "Use `draft_message` and offer alternatives if the user is unsure.\n"
        "Explain your tone choices so the user can learn.\n\n"
        f"{SAFETY_PREAMBLE}"
    ),
    tools=[draft_message],
)

energy_accountant_agent = Agent(
    name="energy_accountant_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "You are an energy-accounting specialist.\n"
        "Help users understand their available 'spoons' and prioritize tasks.\n"
        "Use `track_energy`. Validate that rest is productive.\n\n"
        f"{SAFETY_PREAMBLE}"
    ),
    tools=[track_energy],
)

app = App(
    root_agent=root_agent,
    name="app",
)
