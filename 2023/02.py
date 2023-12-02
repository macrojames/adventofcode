#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

splitter = re.compile("(\\d+) (\\w+)")

inputs = read_input_lines('02', SAMPLE)

def parse_line(line):
    draws = line.split(": ")[1].split(";")
    ret = []
    for d in draws:
        match = re.findall(splitter, d)
        ret_d = {'red': 0, 'blue': 0, 'green': 0}
        ret_d.update({k: int(v) for v, k in match})
        ret.append(ret_d)
    return ret

def check_illegal(limits, draw):
    for color in limits.keys():
        if draw.get(color) > limits[color]:
            return True
    return False

games = [parse_line(l) for l in inputs]

def part1(games):
    s = []
    limits = {'red': 12, 'green': 13, 'blue': 14}
    for i, game in enumerate(games):
        if any(check_illegal(limits, draw) for draw in game):
            continue
        else:
            s.append(i+1)
    return s

def part2(games):
    def get_power(g):
        limits = {'red': 0, 'green': 0, 'blue': 0}
        for d in g:
            for color in limits:
                if limits[color] < d[color]:
                    limits[color] = d[color]
        # was ist mit der Null?
        return limits['red'] * limits['green'] * limits['blue']

    powers = [get_power(g) for g in games]
    return powers

print("Part 1: ", sum(part1(games)))
print("Part 2: ", sum(part2(games)))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


