#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from collections import Counter
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

def part1():
    intlist = [list(map(int, (_.split("   ")))) for _ in inputs]
    list_l, list_r = [sorted([_[0] for _ in intlist]), sorted([_[1] for _ in intlist])]
    return sum([abs(r-l) for l, r in zip(list_l, list_r)])
    
def part2():
    intlist = [list(map(int, (_.split("   ")))) for _ in inputs]
    list_l, list_r = [sorted([_[0] for _ in intlist]), sorted([_[1] for _ in intlist])]
    count_l = Counter(list_l)
    count_r = Counter(list_r)
    s = 0
    for l, c in count_l.items():
        s += (l * count_r[l]) * c  
    return s
    

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

