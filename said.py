"""
Digital Echo
------------
A tiny, creative CLI app that remembers only the last thing you said.
"""

import os

DATA_FILE = "echo.txt"
MAX_LENGTH = 60


def read_last_echo():
    if not os.path.exists(DATA_FILE):
        return None
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def save_echo(text: str):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    last_echo = read_last_echo()

    if last_echo:
        print("Last time you said:")
        print(f"\"{last_echo}\"\n")
    else:
        print("No echo yet. Say something first.\n")

    user_input = input(f"Say something (max {MAX_LENGTH} chars):\n> ").strip()

    if not user_input:
        print("Nothing said. Goodbye.")
        return

    if len(user_input) > MAX_LENGTH:
        print("Too long. Keep it short.")
        return

    save_echo(user_input)
    print("\nYour echo has been saved.")


if __name__ == "__main__":
    main()