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


def move(direction, rocks):
    movements = 0
    new_rocks = set()

    for r, c in sorted(rocks, key=sorter[direction]):
        dr, dc = dirs[direction]
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= len_r or nc < 0 or nc >= len_c:
            new_rocks.add((r, c))    
        elif (nr, nc) not in new_rocks and (nr, nc) not in blocks :
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
    loads = {}
    cycle_offset, cycle_length = None, None
    for i in range(0, 200):
        hashable = tuple(sorted(rs))                                        
        if hashable in positions:  
            cycle_positions = positions[positions.index(hashable):]
            cycle_length = len(cycle_positions)

            goal_pos = (1000000000 - i) % cycle_length
            return loads[ cycle_positions[(goal_pos) % len(cycle_positions)]]
        
        positions.append(hashable)
        for d in ['N', 'W', 'S', 'E']:
            movs = 1
            while movs:
                movs, rs = move(d, rs)
                assert len(rs) == old_len
        k = tuple(sorted(rs)) 
        r=load('N', k)
        loads[k] = r
        print(f"Finished cycle {i:4} with with Load {r=:7}")
    return r   
print(f"Starting with {len(rocks)} rocks")
print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
