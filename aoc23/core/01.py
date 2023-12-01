import re
from curses.ascii import isdigit

from aoc23.input import INPUT_BASE

with open(INPUT_BASE / "01.txt") as fp:
    lines: list[str] = fp.readlines()


def to_digits(s: str) -> str:
    replacement: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    t: list[str] = []
    for key in replacement.keys():
        res = list(re.finditer(key, s))
        for r in res:
            t = list(s)
            # in case e.g. "nineight", we dont want to replace the first "e" in "eight"
            # by "8" to allow finding "nine" in the next iteration.
            t[r.start() + 1] = replacement[key]
            s = "".join(t)
    return "".join(filter(isdigit, s))


lines_filtered_a: list[str] = ["".join(filter(isdigit, line)) for line in lines]
result_a: int = sum(int(line[0] + line[-1]) for line in lines_filtered_a)
print("a: ", result_a)

lines_filtered_b: list[str] = [to_digits(line) for line in lines]
result_b: int = sum(int(line[0] + line[-1]) for line in lines_filtered_b)
print("b: ", result_b)
