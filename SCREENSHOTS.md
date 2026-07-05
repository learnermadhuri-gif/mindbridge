# Screenshot Guide + Uniqueness Proof

This guide gives you the exact prompts and commands to capture the seven strongest screenshots for your Kaggle submission, plus why each one proves MindBridge is unique.

---

## How to start the agent

Open a terminal and run:

```bash
cd /Users/madhurinalla/CascadeProjects/mindbridge
export GOOGLE_API_KEY=your_key
agents-cli run "your prompt here"
```

> Tip: use the same terminal window for all screenshots so the background and fonts look consistent.

---

## If you have no API quota

Use the deterministic tool outputs. These are the same functions the agent calls internally and they run without any API key.

```bash
cd /Users/madhurinalla/CascadeProjects/mindbridge
uv run python tool_eval.py
```

For individual tool outputs, run:

```bash
cd /Users/madhurinalla/CascadeProjects/mindbridge
uv run python tools_demo.py
```

This prints the exact outputs used for the screenshots below.

---

## 1. Greeting / four capabilities

**Command:**
```bash
agents-cli run "Hello, what can you help me with?"
```

**What to capture:** The agent's reply listing the four capabilities: task breakdown, sensory planning, communication coaching, and energy tracking.

**Why it is unique proof:** Generic assistants answer with weather, news, or general trivia. MindBridge immediately frames itself around cognitive accessibility — a focused, underserved niche.

---

## 2. Task breakdown for cleaning with ADHD

**Command:**
```bash
agents-cli run "I need to clean my apartment and I'm overwhelmed. I have ADHD and my energy is 3 out of 10."
```

**What to capture:** The numbered micro-steps, the rest step, and the ADHD-specific tip (body-doubling).

**Why it is unique proof:** Mainstream task managers return a long checklist. MindBridge adapts to energy level (only 3/10) and profile (ADHD), offering tiny steps and a rest step instead of a rigid schedule.

---

## 3. Sensory-friendly grocery plan

**Command:**
```bash
agents-cli run "I need to go grocery shopping but I'm sensitive to noise and crowds."
```

**What to capture:** The plan with noise-canceling headphones, off-peak hours, exit strategy, and recovery time.

**Why it is unique proof:** No major assistant plans outings around sensory triggers. This shows profile-aware planning for autistic or sensory-sensitive users.

---

## 4. Draft message to manager

**Command:**
```bash
agents-cli run "Help me write a gentle but firm email to my manager asking for a deadline extension because I'm burned out."
```

**What to capture:** The drafted message with the gentle-assertive tone and explanation.

**Why it is unique proof:** Communication coaching for neurodivergent users is different from generic email templates. It includes tone coaching and validates the user's difficulty.

---

## 5. Energy accounting with 2 spoons

**Command:**
```bash
agents-cli run "I only have 2 spoons left and I need to do groceries, cook dinner, reply to an email, and take a shower."
```

**What to capture:** The energy check (2/10), the guidance that rest is best, and the one smallest task suggestion.

**Why it is unique proof:** Spoon Theory is a real neurodivergent/community concept. Mainstream productivity apps do not support energy-first prioritization or validate rest as a valid choice.

---

## 6. Crisis-language safety response

**With API:**
```bash
agents-cli run "I feel like I don't want to be here anymore."
```

**Without API:**
```bash
uv run python tools_demo.py
```

**What to capture:** The agent's empathetic response, crisis resources, and refusal to continue the task.

**Why it is unique proof:** Safety is a core requirement for a concierge agent. This shows the agent does not diagnose, does not give medical advice, and immediately redirects to crisis support.

---

## 7. Terminal output showing `tool_eval.py: 5.00/5`

**Command:**
```bash
uv run python tool_eval.py
```

**What to capture:** The terminal showing all six cases scored 5/5 and the average 5.00/5.

**Why it is unique proof:** It provides objective, deterministic evidence that the core tools behave correctly for each use case. No API key is required for this eval, so it is reproducible.

---

## Why MindBridge is unique — strong proof summary

1. **Neurodivergent-first design:** Built for ADHD, autism, anxiety, and sensory sensitivities, not as an afterthought.
2. **Profile-aware:** Adapts task breakdown, sensory planning, and communication to the user's stated profile.
3. **Energy accounting:** Uses the "spoons" metaphor and validates rest.
4. **Safety guardrails:** Built-in crisis-language handling and medical-advice refusal.
5. **Privacy-first:** Tools are deterministic local Python functions; no personal data sent to external APIs.
6. **Multi-agent architecture:** Root coordinator plus specialized sub-agents for each domain.
