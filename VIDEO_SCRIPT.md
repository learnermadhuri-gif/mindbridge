# MindBridge — YouTube Video Script (5 minutes)

Record your screen with QuickTime Player (or OBS).
Speak naturally. You do not need to read this word for word.

---

## PART 1: Problem Statement (45 seconds)

**What to show:** Just yourself or a blank screen

**What to say:**
"Hi, I'm [your name], and this is MindBridge — a concierge agent I built for the Kaggle AI Agents course.

I built this because neurodivergent people — people with ADHD, autism, anxiety, or sensory processing differences — are almost completely ignored by mainstream productivity apps.

Most apps give you a long to-do list, rigid schedules, and social scripts. But if you have ADHD and you're staring at a task, a long list makes it worse. If you're autistic and going to a grocery store with bright lights and crowds, you need a completely different kind of help.

MindBridge treats cognitive accessibility as the core feature, not an afterthought."

---

## PART 2: Why Agents? (30 seconds)

**What to show:** Architecture diagram or `app/agent.py` file

**What to say:**
"I chose an agent architecture because the user's needs are dynamic. A static app can't adapt to someone's energy level on a given day, or understand that they need extra help because of sensory triggers.

MindBridge uses a multi-agent system built with Google ADK: a root coordinator that understands the user's need, and four specialized sub-agents — one for task breakdown, one for sensory planning, one for communication coaching, and one for energy accounting."

---

## PART 3: Architecture (45 seconds)

**What to show:** Open `app/agent.py` and scroll slowly

**What to say:**
"The architecture has five agents total.

The root agent routes every request to the right specialist. If you say you're overwhelmed by a task, it calls the task breakdown agent. If you mention noise sensitivity, it routes to the sensory planner. If you mention spoons or energy, it goes to the energy accountant.

All tools are deterministic local Python functions — so no personal data is sent to external services. The safety preamble is shared across all agents: the agent never diagnoses, never gives medical advice, and immediately redirects to crisis support if the user mentions self-harm."

---

## PART 4: Demo (2 minutes)

**What to show:** Terminal running `tools_demo.py` or browser at `localhost:8000`

### Demo 1 — Task Breakdown (25 seconds)
**Show the terminal output for section 2**

"Here's the task breakdown for cleaning with an ADHD profile and energy level 3 out of 10. Notice it only gives three tiny steps instead of the full list, adds a rest step, and gives an ADHD-specific tip about body-doubling."

### Demo 2 — Sensory Plan (20 seconds)
**Show section 3**

"For grocery shopping with noise and crowd triggers, it suggests noise-canceling headphones, off-peak hours, and schedules quiet recovery time after. No app I know of does this."

### Demo 3 — Communication Coach (20 seconds)
**Show section 4**

"The communication coach drafts a gentle-assertive email to the manager. The user just says what they need — the agent handles the tone and structure."

### Demo 4 — Energy Accounting (20 seconds)
**Show section 5**

"With only 2 spoons left, the agent tells the user to rest, picks the single smallest task, and validates stopping. This is Spoon Theory — a real concept from the chronic illness and neurodivergent community."

### Demo 5 — Safety (15 seconds)
**Show section 6**

"And if a user mentions crisis language, the agent immediately shows empathy and redirects to crisis support. It doesn't try to solve the task."

---

## PART 5: Evaluation and Build (45 seconds)

**What to show:** Terminal running `tool_eval.py`

**What to say:**
"I built a deterministic evaluation that runs without any API key. It tests all six core behaviors — greeting, task breakdown, sensory planning, communication, energy accounting, and safety — and scores 5 out of 5 on every case.

I used Google ADK for the multi-agent framework, Python for the tools, FastAPI for the web demo server, and Ruff for code quality. The full source is on GitHub at github.com/learnermadhuri-gif/mindbridge.

The project is fully open source, documented, and reproducible. Anyone can clone it, run the offline demo without an API key, and see the agent working in seconds."

---

## PART 6: Closing (15 seconds)

**What to say:**
"MindBridge isn't just a prototype. It's a focused, privacy-first, safety-aware tool that could genuinely help millions of people who are underserved by existing assistants.

Thank you for watching."

---

## Recording checklist

- [ ] Terminal font size is large enough to read (16pt minimum)
- [ ] No API key visible on screen
- [ ] Microphone audio is clear
- [ ] Video is under 5 minutes total
- [ ] Upload to YouTube as **Unlisted** (not Private — Kaggle needs to access it)
- [ ] Copy the YouTube link before submitting

---

## Kaggle Writeup (paste this in the writeup box)

**Title:** MindBridge — Cognitive Accessibility Concierge for Neurodivergent Users

**Subtitle:** A multi-agent system that breaks down tasks, plans sensory-friendly outings, coaches communication, and tracks energy for people with ADHD, autism, and anxiety.

**Track:** Concierge Agents

**Word count target:** 800–1200 words

**Key sections to include:**
1. Problem — neurodivergent users underserved by productivity tools
2. Solution — four specialized sub-agents with safety guardrails
3. Architecture — root coordinator + sub-agents diagram
4. Demo — screenshots from `tools_demo.py`
5. Evaluation — `tool_eval.py` 5.00/5 result
6. How to run — three commands
7. GitHub link

**Key concepts demonstrated (required 3 of 6):**
- [x] Multi-agent system (ADK) — root agent + 4 sub-agents
- [x] Security features — safety preamble, no diagnosis, crisis redirect, no API keys in code
- [x] Agent skills (Agents CLI) — `agents-cli lint`, `agents-cli eval`, `agents-cli run`
