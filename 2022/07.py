#!/usr/bin/env python3
from collections import namedtuple
import os
import time
from parse import parse
from pprint import pprint
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

DISKSPACE_AVAIL = 70000000 
DISKSPACE_NEEDED = 30000000 

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

file = namedtuple("File", ["size", "name"])

tree = {"/" : []}
cwd = ""
cd_stack = []

for line in _input:
    if r := parse("$ cd {:S}", line):
        if r[0] == '..':
            cwd = cd_stack.pop()
        else:    
            cd_stack.append(cwd)
            path = f"{cwd}{r[0]}/" if cwd else "/"
            if path not in tree:
                raise Exception("Error", path)
            cwd = path
    elif r := parse("$ ls", line):
        pass
    elif r := parse("dir {:S}", line):
        path = f"{cwd}{r[0]}/" if cwd else "/"
        if path not in tree:
            tree[path] = []
    elif r := parse("{:d} {:S}", line):
        tree[cwd].append(file(r[0], r[1]))

sizes = {p: sum([f.size for f in files]) for p, files in tree.items()}
sizes_rec = {p: size + sum([sizes[key] for key in filter(lambda d: d.startswith(p) and d != p, sizes.keys())]) for p, size in sizes.items()}

filter1 = {k: v for k,v in sizes_rec.items() if v <= 100000}

DISK_FREE = DISKSPACE_AVAIL - sizes_rec["/"]
filter2 = {k: v for k,v in sizes_rec.items() if k != "/" and v >= DISKSPACE_NEEDED-DISK_FREE}

print("Part 1: ", sum(filter1.values()))
print("Part 2: ", min(filter2.values()))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
