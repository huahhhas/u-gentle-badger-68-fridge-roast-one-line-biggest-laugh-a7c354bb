#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Draft: My smart fridge updated its firmware at 3 a.m. and now judges my
midnight snacks with push notifications.
Revised (final): tighter wording, sharper turn — the fridge as a
disappointed IT department beeping at leftovers, not just "judging".
"""

LINE = "My smart fridge updated itself at 3 a.m. and now beeps at my leftovers like a disappointed IT department."

def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
