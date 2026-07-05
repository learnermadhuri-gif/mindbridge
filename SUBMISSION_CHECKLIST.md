# Submission Checklist

Deadline: tomorrow. Use this list to make sure nothing is missing.

## Repository

- [x] Code pushed to GitHub: https://github.com/learnermadhuri-gif/mindbridge
- [ ] Repository is **Public** (check Settings > Visibility on GitHub)
- [x] `README.md` explains the project and how to run it
- [x] `SUBMISSION.md` describes the submission
- [x] `SUBMISSION_REPORT.md` has the evaluation score
- [x] `DEMO.md` and `SCREENSHOTS.md` help reviewers/demo
- [x] Code passes lint: `agents-cli lint`
- [x] Unit tests pass: `uv run pytest tests/test_tools.py`

## Evaluation

- [x] Deterministic tool eval: `uv run python tool_eval.py` → **5.00/5**
- [ ] Agent-level eval: `uv run python local_eval.py` → requires API key with quota
- [x] Report saved: `artifacts/tool_eval_report.json`

## Screenshots or Demo

Choose one:

**A. With API key (if you still have quota or get a new key):**
- [ ] Start web server: `uv run python demo_server.py`
- [ ] Open `http://localhost:8000`
- [ ] Capture the seven interactions from `SCREENSHOTS.md`
- [ ] Optional: record a 60-90 second demo video

**B. Without API key (current plan):**
- [ ] Run `uv run python tools_demo.py`
- [ ] Screenshot the terminal output for each of the 6 cases
- [ ] Run `uv run python tool_eval.py`
- [ ] Screenshot the `Average tool-level score: 5.00/5` output
- [ ] Screenshot the web UI initial page at `http://localhost:8000` (server will start, but responses may fail due to quota)

## Submission Files

- [ ] GitHub repo link
- [ ] README
- [ ] Evaluation report or score screenshot
- [ ] Demo video or screenshots
- [ ] Optional: one-page uniqueness statement

## Final Checks

- [ ] No API key is visible in screenshots or repo
- [ ] Repo is public
- [ ] All links in README work
- [ ] You can explain the four capabilities in 30 seconds
