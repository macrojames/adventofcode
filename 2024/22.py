#!/usr/bin/env python3
from collections import Counter
import time
import os.path
from util import read_input_lines
import colorama

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")


def get_next_num(num):
    num = (int(num * 64) ^ num) % 16777216
    num = (int(num / 32) ^ num) % 16777216
    num = (int(num * 2048) ^ num) % 16777216
    return num


def part1():
    s = 0
    for n in inputs:
        num = int(n)
        for i in range(2000):
            num = get_next_num(num)
        print(n, num)
        s += num
    return s


def part2():
    catalog = {}
    prices = {}
    for n in inputs:
        num = int(n)
        price = [num % 10]
        changes = ""
        for i in range(2000):
            num = get_next_num(num)
            changes += chr(75 + ((num % 10) - price[-1]))
            price.append(num % 10)
        catalog[n] = changes
        prices[n] = price

    x = Counter([y[i : i + 4] for y in catalog.values() for i in range(len(y) - 4)])
    # print(n, num, num % 10, changes[-1])
    # candidates = [k for k, v in x.items() if v > len(inputs) / 2]
    candidates = [k for k, v in x.most_common(1000)]
    yields = {}
    for k in candidates:
        yields[k] = sum([prices[n][catalog[n].index(k) + 4] for n in inputs if k in catalog[n]])
    return max(yields.values())


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
