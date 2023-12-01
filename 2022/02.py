#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
WIN, LOSS, DRAW = 6, 0 ,3

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

points = {"X":1, "Y":2, "Z":3}
outcome = {"X": LOSS, "Y": DRAW, "Z": WIN}
rules = {
    ("A", "X"): DRAW, 
    ("A", "Y"): WIN,
    ("A", "Z"): LOSS,
    ("B", "X"): LOSS, 
    ("B", "Y"): DRAW,
    ("B", "Z"): WIN,
    ("C", "X"): WIN, 
    ("C", "Y"): LOSS,
    ("C", "Z"): DRAW,
}
strat2 = {(_[0], out): points[_[1]] for _, out in rules.items()}
plays = [tuple(_.strip().split(" ")) for _ in _input]

score1 = [rules[p] + points[p[1]] for p in plays]
score2 = [strat2[(p[0], outcome[p[1]])] + outcome[p[1]] for p in plays]

print("Part 1: ", sum(score1))
print("Part 2: ", sum(score2))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
