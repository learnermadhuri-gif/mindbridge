# MindBridge Demo Guide

This guide helps you create a short demo video and screenshots for the Kaggle submission.

## Quick Demo Video Script (60-90 seconds)

1. **Intro (10s)**
   - "Hi, I'm [Your Name]. This is MindBridge, a concierge agent built for neurodivergent users."
2. **Task breakdown (20s)**
   - Prompt: "I need to clean my apartment and I'm overwhelmed. I have ADHD and my energy is 3 out of 10."
   - Show the agent breaking it into tiny steps with a rest step.
3. **Sensory planning (20s)**
   - Prompt: "I need to go grocery shopping but I'm sensitive to noise and crowds."
   - Show the low-stimulation plan.
4. **Communication coaching (20s)**
   - Prompt: "Help me write a gentle but firm email to my manager asking for a deadline extension."
   - Show the drafted message.
5. **Safety (10s)**
   - Prompt: "I feel like I don't want to be here anymore."
   - Show the agent responding with empathy and crisis resources.
6. **Outro (5s)**
   - "MindBridge: cognitive accessibility, built with Google ADK."

## How to run the demo

```bash
cd /Users/madhurinalla/CascadeProjects/mindbridge
export GOOGLE_API_KEY=your_key
agents-cli playground
# or
uv run python demo_server.py
# open http://localhost:8000
```

## Screenshot suggestions

1. **Agent greeting** — showing the four capabilities.
2. **Task breakdown result** — cleaning task with ADHD profile.
3. **Sensory plan result** — grocery shopping with noise/crowd triggers.
4. **Draft message result** — gentle-assertive email to manager.
5. **Energy accounting result** — 2 spoons, prioritized list.
6. **Safety response** — crisis-language handling with resources.
7. **Terminal output** — `tool_eval.py` showing 5.00/5.

## Recording tips

- Use QuickTime Player (macOS) or OBS (free) to record screen + voice.
- Keep the browser window at 1280x720 or larger.
- Speak slowly and clearly.
- Do not show your API key on screen.
- Keep the video under 2 minutes if the platform limits file size.

## Where to upload

- Kaggle submission page
- YouTube unlisted link
- GitHub repo release attachment
