"""The 3AM Fridge Text — entry for make.fun.

Writes one line to /output/entry.txt. The line is the one message a smart fridge would text its owner at 3 AM, at most 140 characters.
"""
import os

LINE = "It's 3 AM. Your leftovers have formed a union and are demanding better lighting. I have locked the door for your own safety."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
