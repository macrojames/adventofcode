#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
from itertools import batched
from collections import deque

start_timer = time.time()

SAMPLE = False
DEBUG = False

inputs = read_input_lines('05', SAMPLE)

s2so, so2f, f2w, w2l, l2t, t2h, h2loc = [], [], [], [], [], [], []
current = None

for line in inputs:
    if line.startswith("seeds"):
        m = re.findall("\\d+", line)
        seeds = list(map(int, m))
        continue
    if line.startswith("seed-to-soil map:"): current = s2so
    elif line.startswith("soil-to-fertilizer map:"): current = so2f
    elif line.startswith("fertilizer-to-water map:"): current = f2w
    elif line.startswith("water-to-light map:"): current = w2l
    elif line.startswith("light-to-temperature map:"): current = l2t
    elif line.startswith("temperature-to-humidity map:"):  current = t2h 
    elif line.startswith("humidity-to-location map:"): current =  h2loc
    elif not line: continue
    else:
        current.append([int(x) for x in line.split(" ")])


def part1():
    locations = []
    for seed in seeds:
        x = seed
        if DEBUG: print(f"Seed: {x:3} ", end="")
        for maps in [s2so, so2f, f2w, w2l, l2t, t2h, h2loc]:
            if DEBUG: print(" | ", end="")
            for m in maps:
                if m[1] <= x < m[1] + m[2]:
                    x = m[0] + (x - m[1])
                    break
                else:
                    pass
                if DEBUG: print(f" -> {x:3}", end="")
        if DEBUG: print(f"  Final: {x}")
        locations.append(x)
    if DEBUG: print(f"  Final-Final: {locations}")
    return locations

def part2():
    for l in [s2so, so2f, f2w, w2l, l2t, t2h, h2loc]: l.sort(key=lambda x:x[1])
    conversions = [s2so, so2f, f2w, w2l, l2t, t2h, h2loc]
    seed_ranges = [(ss, ss + sr) for ss, sr in sorted(batched(seeds, 2))]
    
    for block in conversions:
        if DEBUG: print("------- New Block -------")
        next_ranges = set([])
        for i, (seed_start, seed_end) in enumerate(seed_ranges):
            if DEBUG: print("------- New Seed -------")
            done = False
            for dst, src, r in block:
                if DEBUG: print("------- New Range -------")
                if done: break
                end = src + r
                if DEBUG: print(f"Range: {src:3} - {end:3}: {dst:3} Seed: {seed_start:3} - {seed_end:3}", end=" --> ")
                if seed_end < src or seed_start > end:
                    # komplett außerhalb, nichts ändern
                    next_ranges.add((seed_start, seed_end))
                    if DEBUG: print("Case 1")         
                if seed_start <= end and seed_end >= src:
                    # Treffer in der Range
                    if (seed_start, seed_end) in next_ranges:
                        next_ranges.remove((seed_start, seed_end))
                    hit_start = max(src, seed_start)
                    hit_end = min(end, seed_end)
                    mapped_start = dst + (hit_start - src)
                    mapped_end = mapped_start + (hit_end - hit_start)
                    next_ranges.add((mapped_start, mapped_end))
                    if DEBUG: print("Case 4", end=" ")

                    if seed_start < src and seed_end > src:
                        # es hängt links über, abschneiden
                        next_ranges.add((seed_start, src - seed_start))
                        if DEBUG: print("Case 2", end=" ")
                    if seed_start < end and seed_end > end:
                        # es hängt rechts über, abschneiden
                        seed_ranges.insert(i + 1, (end + 1 , seed_end))
                        if DEBUG: print("Case 3", end=" ")
                    done = True
                if DEBUG: print()

            if DEBUG: print(next_ranges)
        
        seed_ranges = sorted(next_ranges, key=lambda x:x[0])
    return seed_ranges[0][0] - 1


print("Part 1: ", min(part1()))
print("Part 2: ", part2())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


