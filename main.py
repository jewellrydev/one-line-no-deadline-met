"""One Line, No Deadline Met — a make.fun entry.

Prints exactly one single-line joke giving an excuse for missing a
deadline, capped at 200 characters.
"""

LINE = (
    "The deadline wasn't missed; it was strategically relocated to "
    "a date where it can become someone else's emergency."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
