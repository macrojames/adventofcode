#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from collections import defaultdict, deque
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = False
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

diskmap = list(map(int, (c for c in inputs[0])))
free = defaultdict(list)
files = {}

address = 0
file_id = 0

fulldisk = [None] * sum(diskmap)

for i, size in enumerate(diskmap):
    if i % 2 == 0:
        # file
        if size:
            files[file_id] = (address, size)
            fulldisk[address:address+size] = [file_id] * size
            file_id += 1
    else:
        if size > 0:
            free[size].append(address)
        # free space
    address += size

def part1(disk):
    pos = len(disk) - 1
    while pos > disk.index(None):
        if file_id := disk[pos]:
            # find spot
            disk[disk.index(None)] = file_id
            disk[pos] = None
        pos -= 1
    ret = 0
    for i in range(disk.index(None)):
        ret += (i * disk[i])
    return ret

def part2(disk):
    for file_id in sorted(files.keys(), reverse=True):
        address, size = files[file_id]
        pos = address
        check_size = None

        for sz, free_addresses in free.items():
            if sz >= size and min(free_addresses) < pos:
                pos = min(free_addresses)
                check_size = sz       
        if not check_size:
            continue
           
        disk[pos:pos+size] = [file_id] * size
        disk[address:address+size] = [None] * size

        free[check_size].remove(pos)
        if size < check_size:
            free[check_size - size].append(pos + size)

    ret = 0
    for i, s in enumerate(disk):
        if s:
            ret += (i * s)
    return ret



print("Part 1: ", part1(disk=fulldisk[:]))
print("Part 2: ", part2(disk=fulldisk[:]))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

