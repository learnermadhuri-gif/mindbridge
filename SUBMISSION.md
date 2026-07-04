# MindBridge — Kaggle AI Agents Competition Submission

## Track

**Concierge Agents**

## Problem

Neurodivergent people (ADHD, autism, anxiety, sensory processing differences) are underserved by mainstream productivity assistants. Most tools assume a neurotypical workflow: long task lists, rigid schedules, and social scripts that feel unnatural. Existing assistants treat cognitive accessibility as an afterthought, which increases overwhelm rather than reducing it.

## Solution

**MindBridge** is the first concierge agent built specifically around cognitive accessibility. It adapts to the user's neurodivergent profile and helps with four everyday challenges:

1. **Task breakdown** — turns overwhelming tasks into tiny, doable micro-steps with timers and rewards.
2. **Sensory-friendly planning** — recommends low-stimulation times, environments, and coping tools.
3. **Communication coaching** — drafts difficult messages with tone options tailored to the user's needs.
4. **Energy accounting** — helps users prioritize based on remaining "spoons" and validates rest.

## Why It Is Unique

- **Neurodivergent-first design** — not a generic assistant with an "accessibility" label.
- **Profile-aware** — explicitly optimizes for ADHD, autism, anxiety, and sensory sensitivities.
- **Multi-agent architecture** — root coordinator plus specialized sub-agents for each domain.
- **Privacy-first** — no cloud storage of personal profiles by default; sessions are in-memory.
- **Safety guardrails** — refuses to diagnose, includes crisis disclaimers, and respects autonomy.

## Real-World Usefulness

- Helps an ADHD user start cleaning when they are frozen by overwhelm.
- Helps an autistic user plan a grocery trip that avoids sensory overload.
- Helps an anxious user draft a firm but kind message to a manager.
- Helps a burned-out user decide which one task to do with limited energy.

## Technical Design

- **Framework:** Google ADK (Agent Development Kit)
- **Language:** Python 3.11+
- **Model:** `gemini-2.5-flash-lite` (fast, cost-effective, avoids the exhausted `gemini-3.5-flash` free tier)
- **Architecture:**
  - `root_agent` — routes requests and welcomes users
  - `task_breakdown_agent` — decomposes tasks
  - `sensory_planner_agent` — plans low-stimulation outings
  - `communication_coach_agent` — drafts messages
  - `energy_accountant_agent` — prioritizes by energy
- **Tools:** deterministic, local Python functions (no external API dependencies)
- **Safety:** shared safety preamble across all agents; crisis-language handling
- **Eval:** `tests/eval/datasets/basic-dataset.json` with custom response quality + safety metrics
- **Fallback eval:** `tool_eval.py` runs deterministic tool-level checks without any API key (average 5.00/5)

## How to Run

1. Copy `.env.example` to `.env` and add a Gemini API key.
2. Run `agents-cli install`.
3. Run `agents-cli playground` for an interactive chat UI.
4. Run `agents-cli run "your prompt"` for a one-off test.
5. Run `agents-cli eval run` to evaluate behavior.

## Demo

See `demo.py` for an offline tool demonstration (no API key required).

## Team

Individual submission.
