#!/usr/bin/env python3
from functools import cache
import time
import os.path
from util import read_input_lines
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")
if SAMPLE:
    devices = {line.split(":")[0]:
        [_ for _ in line.split(":")[1].split(" ") if _ != ""]
        for line in inputs[:10]
    }
    devices2 = {line.split(":")[0]:
        [_ for _ in line.split(":")[1].split(" ") if _ != ""]
        for line in inputs[11:]
    }
else:
    devices = {line.split(":")[0]:
        [_ for _ in line.split(":")[1].split(" ") if _ != ""]
        for line in inputs
    }
    devices2 = devices
    
@cache
def find_ways(start, end):
    visited={}
    if start not in devices: return {start: 0}
    targets = devices[start]
    
    if end in targets: return {start: 1}
    else:
        result = 0
        for target in targets:
            x = find_ways(target, end)
            result += x[target]
            visited.update(x)
        if start not in visited:
            visited[start] = 0
        visited[start] += result
    return visited

def part1():    
    p = find_ways("you", "out")
    return p["you"]


def part2():
    global devices
    devices = devices2
    p = find_ways("svr", "fft")["svr"]
    q = find_ways("fft", "dac")["fft"]
    r = find_ways("dac", "out")["dac"]
    return p*q*r

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

