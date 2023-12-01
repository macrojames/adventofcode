#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)
moves = [(l.split(" ")[0], int(l.split(" ")[1])) for l in _input]

Tx = Ty = Hx = Hy = 0


def follow(rope, index_front, index_back):
    Hx, Hy = rope[index_front]
    Tx, Ty = rope[index_back]
    if Tx == Hx and abs(Hy - Ty) > 1:
        Ty += int((Hy-Ty) / abs(Hy-Ty))
    elif Ty == Hy and abs(Hx - Tx) > 1:
        Tx += int((Hx-Tx) / abs(Hx-Tx))
    else:                   # diagonal
        if abs(Hy - Ty) > 1 and abs(Hx - Tx) > 1:
            Tx += int((Hx-Tx) / abs(Hx-Tx))
            Ty += int((Hy-Ty) / abs(Hy-Ty))
        elif abs(Hy - Ty) > 1:
            Tx = Hx
            Ty += int((Hy-Ty) / abs(Hy-Ty))
        elif abs(Hx - Tx) > 1:
            Ty = Hy
            Tx += int((Hx-Tx) / abs(Hx-Tx))
    rope[index_back] = [Tx, Ty]
    

def simulate(rope):
    visited = set()
    for dir, steps in moves:
        if DEBUG:
            print("==", dir, steps, "==")
            print()
        for step in range(steps):
            if dir == 'U':
                rope[0][1] += 1
            elif dir == 'D':
                rope[0][1] -= 1
            elif dir == 'L':
                rope[0][0] -= 1
            elif dir == 'R':
                rope[0][0] += 1
            for i in range(1, len(rope)):
                follow(rope, i-1, i)
                #print_state(rope, i)
            visited.add((rope[-1][0], rope[-1][1]))
            if DEBUG:
                print_state(rope)
    return visited

def print_state(rope, active=-1):
    for y in range(15, -6, -1):
        for x in range(-11,15):
            num = False
            for i in range(len(rope)):
                if not num and x == rope[i][0] and y == rope[i][1]:
                    print("H" if i == 0 else "*" if i == active else i, end="")
                    num = True
            if not num and x == 0 and y == 0:
                print("s", end="")
            elif not num:
                print(".", end="")
        print()
    print()

def make_rope(l):
    return [[0,0] for _ in range(l)]

print("Part 1: ", len(simulate(make_rope(2))))
print("Part 2: ", len(simulate(make_rope(10))) )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")

