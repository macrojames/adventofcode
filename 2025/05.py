#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines, read_input_raw
import colorama

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_raw(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")
ranges = [tuple(map(int, l.split("-"))) for l in inputs.split("\n\n")[0].split("\n")]
nums = [int(l) for l in inputs.split("\n\n")[1].split("\n")]


def part1():
    return sum([1 for n in nums if any(l <= n <= r for l, r in ranges)])


def compress(ranges):
    changed = False
    combined = []
    ranges = sorted(ranges)
    while ranges:
        l, r = ranges.pop(0)
        included = [_ for _ in ranges if _[0] <= r]
        if included:
            for inc in included:
                changed = True
                r = max(r, inc[1])
                ranges.remove(inc)
        combined.append((l, r))
    if changed:
        return compress(combined)
    else:
        return combined


def part2():
    combined = compress(ranges)
    return sum([r - l + 1 for l, r in combined])


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
