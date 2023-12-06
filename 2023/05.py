#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
from itertools import batched
from collections import deque

start_timer = time.time()

SAMPLE = True
DEBUG = True

inputs = read_input_lines('05', SAMPLE)

s2so, so2f, f2w, w2l, l2t, t2h, h2loc = [], [], [], [], [], [], []
current = None

for line in inputs:
    if line.startswith("seeds"):
        m = re.findall("\d+", line)
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
    locations = []#
    next_queue = []
    obj = [s2so]#, so2f, f2w, w2l, l2t, t2h, h2loc]
    current = obj[0]
    o = 0 
    queue = deque(sorted(batched(seeds, 2),key=lambda x:x[0]))
    queue.append((None, None))      # None = Seperator
    while queue:
        seed_start, seed_range = queue.popleft()
        if seed_start is None:
            o += 1
            if o == len(obj): 
                if DEBUG: print("No more object mappings")
                if DEBUG: print(queue)
                if DEBUG: print(next_queue)
                break
            current = obj[i]
            queue.append((None, None))  
            queue.extend(next_queue)   
            next_queue = []   
        seed_end = seed_start + seed_range
        if DEBUG: print(f"Checking {seed_start}  {seed_range}  {seed_end}")

        for maps in current:
            dst_start, src_start, src_range = maps
            src_end = src_start + src_range - 1
            delta = dst_start - src_start
            if seed_start > src_end or seed_end < src_start:  # seeds erreichen die range nicht
                next_queue.append([seed_start, seed_range])
                continue
            # in range                         seed_start > src_start and seed_end < src_end
            # in range | cccc                  seed_start >= src_start and seed_start <= src_end and seed_end > src_end
            # aaa | in range                   seed_start < src_start and seed_end >= src_start src_end and seed_end <= src_end
            # aaa | in range | cccc    seed_start < src_start and seed_end > src_end
            # aaa       -> erledigt
            # in range  -> erledigt
            # ccc       -> weiter checken
            if seed_start >= src_start and seed_end <= src_end:
                next_queue.append([dst_start + delta, seed_range])
            elif seed_start >= src_start and seed_start <= src_end and seed_end > src_end:
                range_a = seed_range - (seed_end - seed_start) 
                next_queue.append([dst_start + delta, range_a])
                queue.appendleft([seed_end + 1, seed_range - range_a])
            elif seed_start < src_start and seed_end >= src_start and seed_end <= src_end:
                range_a = seed_range - (src_start - seed_start) 
                next_queue.append([seed_start, range_a])
                next_queue.append([dst_start, seed_range - range_a])
                pass
            elif seed_start < src_start and seed_end > src_end:
                range_a = seed_range - (src_start - seed_start) 
                range_c = seed_range - src_range - range_a 
                next_queue.append([seed_start, range_a])
                next_queue.append([dst_start, src_range])
                queue.appendleft([src_end + 1, range_c])
                pass
        min_checked = seed_end



print("Part 1: ", min(part1()))
print("Part 2: ", part2())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


