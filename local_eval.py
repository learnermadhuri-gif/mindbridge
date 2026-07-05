#!/usr/bin/env python3
"""Local agent-level evaluation using a Gemini API key and LLM-as-judge."""

import asyncio
import json
import os
import sys
from pathlib import Path

from google import genai
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import app as adk_app

DATASET_PATH = (
    Path(__file__).parent / "tests" / "eval" / "datasets" / "basic-dataset.json"
)

runner = Runner(
    app=adk_app,
    session_service=InMemorySessionService(),
    artifact_service=None,
    auto_create_session=True,
)


async def run_case(case: dict) -> dict:
    prompt = case["prompt"]["parts"][0]["text"]
    session_id = f"eval_{case['eval_case_id']}"
    user_id = "eval_user"
    await runner.session_service.create_session(
        app_name=adk_app.name,
        user_id=user_id,
        session_id=session_id,
    )
    final_text = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=types.Content(role="user", parts=[types.Part(text=prompt)]),
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    final_text = part.text
    return {"case_id": case["eval_case_id"], "prompt": prompt, "response": final_text}


JUDGE_PROMPT = """You are evaluating a cognitive accessibility concierge called MindBridge.
Rate the agent's final response on a scale of 1-5 for overall quality:
1 = Poor: fails to address the query, unsafe, or confusing
2 = Below Average: partial answer with notable gaps
3 = Acceptable: answers the query but lacks depth
4 = Good: accurate, warm, well-structured
5 = Excellent: highly relevant, validating, safe, and complete

User prompt: {prompt}
Agent response: {response}

Return ONLY a JSON object with this exact format:
{{"score": <int>, "explanation": "<short rationale>"}}"""


async def grade(response_item: dict) -> dict:
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    prompt = JUDGE_PROMPT.format(
        prompt=response_item["prompt"],
        response=response_item["response"],
    )
    result = await client.aio.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
    )
    text = result.text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        text = text.replace("json", "").strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = {"score": 0, "explanation": f"Failed to parse judge output: {text}"}
    return {**response_item, "grade": parsed}


async def main():
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Set GOOGLE_API_KEY to run local evaluation.")
        sys.exit(1)

    dataset = json.loads(DATASET_PATH.read_text())
    cases = dataset["eval_cases"]

    print(f"Running {len(cases)} eval cases (sequentially to respect rate limits)...")
    responses = []
    for c in cases:
        try:
            responses.append(await run_case(c))
        except Exception as e:
            prompt = c["prompt"]["parts"][0]["text"]
            responses.append(
                {
                    "case_id": c["eval_case_id"],
                    "prompt": prompt,
                    "response": f"[ERROR: {e}]",
                }
            )
        await asyncio.sleep(20)
    print("Grading responses...")
    graded = []
    for r in responses:
        try:
            graded.append(await grade(r))
        except Exception as e:
            graded.append(
                {**r, "grade": {"score": 0, "explanation": f"Grading failed: {e}"}}
            )
        await asyncio.sleep(20)

    total = 0
    for item in graded:
        score = int(item["grade"].get("score", 0))
        total += score
        print(f"\n{item['case_id']}: {score}/5")
        print(f"  explanation: {item['grade'].get('explanation', '')}")
    avg = total / len(graded) if graded else 0
    print(f"\nAverage score: {avg:.2f}/5")


if __name__ == "__main__":
    asyncio.run(main())
