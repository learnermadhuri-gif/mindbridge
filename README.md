# MindBridge

**Track:** Concierge Agents  
**Tagline:** A cognitive accessibility concierge for neurodivergent users.

MindBridge is an AI agent built for people with ADHD, autism, anxiety, and sensory processing differences. Instead of treating neurodivergence as an afterthought, it is designed from the ground up to reduce overwhelm, support executive function, and help users navigate everyday tasks with dignity.

## What makes it unique

- **Neurodivergent-first design** — not a generic productivity app with an accessibility label.
- **Profile-aware assistance** — adapts responses to ADHD, autism, anxiety, or sensory-sensitivity profiles.
- **Multi-agent architecture** — specialized sub-agents for task breakdown, sensory planning, communication coaching, and energy accounting.
- **Privacy-first** — personal profiles and sessions stay in-memory by default; no cloud storage required.
- **Safety guardrails** — never diagnoses, includes crisis disclaimers, and respects user autonomy.

## Capabilities

1. **Task breakdown** — turns overwhelming tasks (e.g., "clean my apartment") into tiny, doable steps with timers and rewards.
2. **Sensory-friendly planning** — suggests low-stimulation times, environments, and coping tools for outings.
3. **Communication coaching** — drafts difficult messages with tone options (gentle-assertive, direct, apologetic, warm).
4. **Energy accounting** — helps users prioritize tasks based on remaining "spoons."

## Project Structure

```
mindbridge/
├── app/
│   ├── agent.py          # Main agent logic and tools
│   ├── fast_api_app.py   # FastAPI serving layer
│   └── app_utils/        # A2A, telemetry, sessions
├── tests/                # Unit tests
├── .agents-cli-spec.md   # Agent specification
├── .env.example          # Example environment variables
└── pyproject.toml        # Dependencies
```

## Requirements

- **uv**: Python package manager — [Install](https://docs.astral.sh/uv/getting-started/installation/)
- **agents-cli**: `uv tool install google-agents-cli`
- **Google Gemini API key**: Get one at [Google AI Studio](https://aistudio.google.com/app/apikey)
  - Note: free-tier keys have strict daily limits. For full `agents-cli eval` or a polished demo, use a billing-enabled Google Cloud project.

## Quick Start

1. Copy the environment file and add your API key:

```bash
cp .env.example .env
# Edit .env and set GOOGLE_API_KEY=your_key_here
```

2. Install dependencies:

```bash
agents-cli install
```

3. Run the agent:

```bash
agents-cli playground
```

Or test a single prompt:

```bash
agents-cli run "I need to clean my apartment and I'm overwhelmed"
```

Or run the standalone demo server with a built-in web chat UI:

```bash
uv run python demo_server.py
# open http://localhost:8000
```

> **Note:** `.env` is gitignored for safety. Copy `.env.example` to `.env` and fill in your API key before running the live agent.

## Example interactions

```
User: I need to clean my apartment and I'm overwhelmed
Agent: That sounds hard. Let's make it tiny. What kind of task is it?
        I can break it down for ADHD, autism, anxiety, or sensory profiles.

User: I only have 3 spoons left and I need to do groceries, email my boss, and cook
Agent: [uses track_energy to suggest the smallest task and validate rest]

User: Help me write an email to my boss asking for a deadline extension
Agent: [uses draft_message to produce a gentle-assertive draft]
```

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli eval`    | Evaluate agent behavior (generate, grade, analyze, and more — see `agents-cli eval --help`) |
| `uv run pytest tests/unit tests/integration` | Run unit and integration tests                                                        |
| `uv run python tool_eval.py` | Run deterministic tool-level evaluation (no API key required) |
| `uv run python local_eval.py` | Run agent-level evaluation with LLM-as-judge (requires API key with quota) |
| [A2A Inspector](https://github.com/a2aproject/a2a-inspector) | Launch A2A Protocol Inspector |

## Evaluation

The deterministic tool evaluation scores **5.00/5** on the default dataset:

```bash
uv run python tool_eval.py
```

This is the primary, reproducible evaluation because it does not require any API key.

The agent-level LLM-as-judge evaluation in `local_eval.py` is available for reviewers with a billing-enabled Google Cloud project or a paid API key. The Gemini free tier is limited to 20 requests/day per model per project, which is not enough for a full 12-call eval run.

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.

## A2A Inspector

This agent supports the [A2A Protocol](https://a2a-protocol.org/). Use the [A2A Inspector](https://github.com/a2aproject/a2a-inspector) to test interoperability.
See the [A2A Inspector docs](https://github.com/a2aproject/a2a-inspector) for details.
