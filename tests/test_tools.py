"""Tests for MindBridge tools."""

from app.agent import (
    break_down_task,
    draft_message,
    get_current_time,
    suggest_sensory_friendly_plan,
    track_energy,
)


def test_break_down_task_returns_steps():
    result = break_down_task("clean my apartment", energy_level=5, profile="adhd")
    assert "1." in result
    assert "Tip" in result
    assert "body-doubling" in result


def test_break_down_task_low_energy_truncates():
    result = break_down_task("clean my apartment", energy_level=2, profile="adhd")
    lines = [line for line in result.split("\n") if line.strip().startswith("1.")]
    assert lines
    assert "Rest step" in result


def test_suggest_sensory_friendly_plan_includes_triggers():
    result = suggest_sensory_friendly_plan(
        "grocery shopping", "noise, crowds", "downtown"
    )
    assert "noise" in result.lower()
    assert "off-peak" in result.lower()
    assert "recovery" in result.lower()


def test_draft_message_has_parts():
    result = draft_message("boss", "I need a deadline extension", "direct")
    assert "Hi boss" in result
    assert "I need a deadline extension" in result
    assert "direct" in result


def test_track_energy_prioritizes_low_energy():
    result = track_energy(2, "groceries, cook, laundry")
    assert "2/10" in result
    assert "Rest is the best choice" in result
    assert "smallest task" in result


def test_get_current_time_returns_string():
    result = get_current_time("now")
    assert isinstance(result, str)
    assert len(result) > 0
