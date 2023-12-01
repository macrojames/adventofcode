#!/usr/bin/env python3
from copy import copy
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

numbers = {'zero': 0,
    'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9
}

digits = [str(s) for s in numbers.values()]
inp = read_input_lines('01', SAMPLE)


def sum1(inp) -> int :
    sum1 = 0
    for line in inp:
        n = ''
        for c in line:
            if c in digits:
                n += c
                break
        for c in line[::-1]:
            if c in digits:
                n += c
                break
        
        if len(n) == 2:
            sum1 += int(n)
    return sum1

def sum2(inp) -> int :
    sum2 = 0
    for line in inp:
        n = ''
        for i, c in enumerate(line):
            part = line[:i+1]
            if c in digits:
                n += c
                break
            elif any([k in part for k in numbers.keys()]):
                x = next(v[1] for v in numbers.items() if v[0] in part)
                n += str(x)
                break
        for i, c in enumerate(line[::-1]):
            part = line[::-1][:i+1]
            if c in digits:
                n += c
                break
            elif any([k[::-1] in part for k in numbers.keys()]):
                x = next(v[1] for v in numbers.items() if v[0][::-1] in part)
                n += str(x)
                break
        
        if len(n) == 2:
            sum2 += int(n)        
    return sum2

print("Part 1: ", sum1(inp))
inp = read_input_lines('01', SAMPLE, part=2)
print("Part 2: ", sum2(inp))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


