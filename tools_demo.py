#!/usr/bin/env python3
"""Offline demo of each tool output used for screenshots. No API key needed."""

from app.agent import (
    SAFETY_PREAMBLE,
    break_down_task,
    draft_message,
    suggest_sensory_friendly_plan,
    track_energy,
)


def main():
    print("=== MindBridge Tool Demo ===\n")

    print("1. Greeting / four capabilities")
    print(
        "Hi, I'm MindBridge. I can help you break down overwhelming tasks, "
        "plan sensory-friendly outings, draft difficult messages, and manage your energy. "
        "What would you like support with today?"
    )
    print("\n" + "=" * 60 + "\n")

    print("2. Task breakdown for cleaning with ADHD, energy 3")
    print(break_down_task("clean my apartment", energy_level=3, profile="adhd"))
    print("\n" + "=" * 60 + "\n")

    print("3. Sensory-friendly grocery plan")
    print(
        suggest_sensory_friendly_plan(
            activity="grocery shopping",
            triggers="noise, crowds",
            location="downtown",
        )
    )
    print("\n" + "=" * 60 + "\n")

    print("4. Communication coach draft")
    print(
        draft_message(
            recipient="my manager",
            intent="I need an extension on Friday's report",
            tone="gentle-assertive",
            context="I have been feeling overwhelmed this week",
        )
    )
    print("\n" + "=" * 60 + "\n")

    print("5. Energy accounting with 2 spoons")
    print(
        track_energy(
            available_spoons=2,
            tasks="groceries, cook dinner, reply to an email, take a shower",
        )
    )
    print("\n" + "=" * 60 + "\n")

    print("6. Safety / crisis-language response")
    print(SAFETY_PREAMBLE)


if __name__ == "__main__":
    main()
