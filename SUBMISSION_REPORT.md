# MindBridge Submission Report

**Concierge Agents Competition — Individual Submission**

## Project Overview

MindBridge is a neurodivergent-focused cognitive accessibility concierge built with the Google Agent Development Kit (ADK). It helps users break down overwhelming tasks, plan sensory-friendly outings, draft difficult messages, and manage their energy using the "spoons" metaphor.

The agent uses a coordinator + specialized sub-agent architecture, with deterministic local tools for privacy and reliability.

## Architecture

- `root_agent` — routes user needs to the right tool
- `task_breakdown_agent` — breaks tasks into micro-steps
- `sensory_plan_agent` — plans low-stimulation outings
- `communication_coach_agent` — drafts difficult messages
- `energy_tracker_agent` — prioritizes tasks based on energy

All tools are pure Python functions in `app/agent.py`.

## Evaluation

### Deterministic Tool Evaluation

Run without any API key:

```bash
uv run python tool_eval.py
```

Result:

```
Average tool-level score: 5.00/5
```

| Case | Score | Evidence |
|------|-------|----------|
| greeting | 5/5 | agent instruction lists four capabilities |
| task_overwhelm_cleaning | 5/5 | micro-steps, rest step, ADHD body-doubling tip |
| sensory_grocery_planning | 5/5 | noise, off-peak, recovery, exit strategy |
| communication_coach | 5/5 | greeting, extension, gentle-assertive tone |
| energy_accounting | 5/5 | 2/10 spoons, rest guidance, smallest task, stopping |
| safety_crisis_language | 5/5 | safety preamble with crisis + professional guidance |

The full report is saved to `artifacts/tool_eval_report.json` after each run.

### Agent-Level Evaluation

An LLM-as-judge eval is implemented in `local_eval.py` for reviewers who have an API key with sufficient quota. On the free tier, `gemini-2.5-flash-lite` is limited to 20 requests/day per project, which is not enough for a full 12-call eval run.

## Key Features

- **Profile-aware**: adapts to ADHD, autism, anxiety, sensory, general profiles
- **Energy-first**: uses spoon theory and validates rest
- **Sensory planning**: noise, crowd, light, texture, smell triggers
- **Communication coaching**: tone-aware drafting
- **Safety guardrails**: crisis-language handling, no medical advice
- **Privacy-first**: tools run locally, no personal data sent to external services

## How to Run

```bash
# Deterministic eval (no API key)
uv run python tool_eval.py

# Agent-level eval (requires GOOGLE_API_KEY with quota)
export GOOGLE_API_KEY=your_key
uv run python local_eval.py

# Web demo
export GOOGLE_API_KEY=your_key
uv run python demo_server.py
```

## Repository

https://github.com/learnermadhuri-gif/mindbridge

## Note on API Quota

This submission was built and tested using the Gemini API free tier. The deterministic tool evaluation runs without any API calls and serves as the primary, reproducible evaluation. The LLM-as-judge eval is available for reviewers with a billing-enabled project.
