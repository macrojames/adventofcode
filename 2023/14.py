#!/usr/bin/env python3
import functools
import time
import os.path
from util import read_input_lines

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

blocks, rocks = set(), set()
for r, line in enumerate(inputs):
    for c, char in enumerate(line):
        if char == 'O': rocks.add((r,c))
        elif char == '#': blocks.add((r,c))
len_r = len(inputs)
len_c = len(inputs[0])

dirs = {'S': (1, 0), 'N': (-1, 0), 'W': (0, -1), 'E': (0, 1)}
sorter = {'N': lambda x: ( x[0], x[1]), 
          'S': lambda x: (-x[0], x[1]), 
          'W': lambda x: ( x[1], x[0]), 
          'E': lambda x: (-x[1], x[0])}

@functools.cache
def move(direction, rocks):
    movements = 0
    new_rocks = set()

    for r, c in sorted(rocks, key=sorter[direction]):
        dr, dc = dirs[direction]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= len_r or nc < 0 or nc >= len_c:
            new_rocks.add((r, c))    
        elif (nr, nc) not in blocks and (nr, nc) not in new_rocks:
            new_rocks.add((nr, nc))
            movements += 1
        else:
            new_rocks.add((r, c))

    return movements, new_rocks

def load(direction, rocks):
    if direction == 'N':
        return sum(len_r - r for r,c in rocks)

def print_grid(rocks):
    for r, line in enumerate(inputs):
        for c, _ in enumerate(line):
            if (r, c) in rocks: char = 'O'
            elif (r, c) in blocks: char = '#'
            else: char = '.'
            print(char, end="")
        print()

def part1():
    movs = 1
    r = 0
    rs = rocks
    while movs:
        movs, rs = move('N', tuple(rs))
        #print(f"Movements: {movs}")
        r=load('N', rs)
        #print(f"Load: {r}")
    return r
    #print_grid()

def part2():
    rs = rocks
    old_len = len(rocks)
    positions = []
    for i in range(1000):
        for d in ['N', 'W', 'S', 'E']:
            movs = 1
            while movs:
                movs, rs = move(d, tuple(sorted(rs)))
                assert len(rs) == old_len
        r=load('N', rs)
        print(f"Finished cycle {i:4} with Load {r:7} for {len(rocks)} rocks")
        hashable = tuple(sorted(rs))
        if not hashable in positions: positions.append(hashable)
        else: 
            #print(f"Finished cycle {i:4} with repeating starting position @ {positions.index(hashable)}")
            cycle_length = i-positions.index(hashable)
            cycle_offset = positions.index(hashable)
            target_pos = 1 + (1000000000 - cycle_offset) % cycle_length
            r = load('N', positions[target_pos])
            print(f"Should be cycle {target_pos} @ load={r}")
            break
    return r   
print(f"Starting with {len(rocks)} rocks")
print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
