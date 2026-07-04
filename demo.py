#!/usr/bin/env python3
"""Offline demo of MindBridge tools."""

from app.agent import (
    break_down_task,
    draft_message,
    suggest_sensory_friendly_plan,
    track_energy,
)


def main():
    print("=== MindBridge offline tool demo ===\n")

    print("1. Task breakdown for cleaning with low energy:")
    print(break_down_task("clean my apartment", energy_level=3, profile="adhd"))
    print("\n" + "=" * 50 + "\n")

    print("2. Sensory-friendly grocery plan:")
    print(
        suggest_sensory_friendly_plan(
            activity="grocery shopping",
            triggers="noise, crowds, bright lights",
            location="downtown",
        )
    )
    print("\n" + "=" * 50 + "\n")

    print("3. Communication coach draft:")
    print(
        draft_message(
            recipient="my manager",
            intent="I need an extension on Friday's report",
            tone="gentle-assertive",
            context="I have been feeling overwhelmed this week",
        )
    )
    print("\n" + "=" * 50 + "\n")

    print("4. Energy accounting with 3 spoons:")
    print(
        track_energy(
            available_spoons=3,
            tasks="groceries, email boss, cook dinner, laundry",
        )
    )


if __name__ == "__main__":
    main()
