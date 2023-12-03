#!/usr/bin/env python3
from math import prod
import time
import re
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

inputs = read_input_lines('03', SAMPLE)

arr = []
numbers = {}
symbols = {}
symbols_numbers = {}

max_r, max_c = len(inputs), len(inputs[0])

for r, line in enumerate(inputs):
    number = ''
    pos = ()
    for c, s in enumerate(line):
        if s.isnumeric():
            if not number:
                pos = (r, c)
            number += s
        elif number:
            numbers[pos] = number
            number = ''
        if not s.isnumeric() and s != '.':
            symbols[(r, c)] = s
    if number:    # end of line
        numbers[pos] = number

def get_atleast_one_symbol(x):
    (r, c), number = x     # len = 3, (0,0) -> (0-3, 0), (0-3, 1)
    neighbors = []
    sym = False
    for d_r in [r - 1, r, r + 1]:
        if d_r < 0 or d_r >= max_r: continue    #oob
        for d_c in range(c - 1, c + len(number) + 1):
            if d_c < 0 or d_c >= max_c: continue     #oob
            if d_r == r and c <= d_c  < c + len(number): continue #in number
            if (d_r, d_c ) in symbols:
                sym = True
                # Hack for part 2
                if symbols[(d_r, d_c)] == '*':
                    if not (d_r, d_c ) in symbols_numbers:
                        symbols_numbers[(d_r, d_c)] = []
                    symbols_numbers[(d_r, d_c)].append(int(number))
    return sym


def part1():
    return [n[1] for n in numbers.items() if get_atleast_one_symbol(n)]

def part2():
    return [prod(n) for n in symbols_numbers.values() if len(n) > 1]


print("Part 1: ", sum(int(x) for x in part1()))
print("Part 2: ", sum(part2()))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


