#!/usr/bin/env python3
from enum import Enum
import os
import time
import re
from util import read_input_raw
start_timer = time.time()

SAMPLE = False


class Direction(object):
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    UP = (0, -1)

    def __init__(self, init) -> None:
        self.current = init

    def turn(self, turning) -> tuple:
        # autopep8: off 
        if self.current == Direction.RIGHT: self.current = Direction.DOWN if turning == 'R' else Direction.UP
        elif self.current == Direction.DOWN: self.current = Direction.LEFT if turning == 'R' else Direction.RIGHT
        elif self.current == Direction.LEFT: self.current = Direction.UP if turning == 'R' else Direction.DOWN
        elif self.current == Direction.UP: self.current = Direction.RIGHT if turning == 'R' else Direction.LEFT
        return self.current
        # autopep8: on
    @property
    def value(self):
        return {self.RIGHT:0, self.DOWN:1, self.LEFT:2, self.UP:3}[self.current]

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_raw(day, SAMPLE)
grid_lines = [list(_) for _ in _input.splitlines()[:-2]]
width = max(map(len, grid_lines))
edges = []
blocks = []

direction = Direction(Direction.RIGHT)
for y, line in enumerate(grid_lines):
    right_offset = width - len(line)
    left_end = min([i for i, x in enumerate(line) if x in ['.', '#']])
    right_end = max([i for i, x in enumerate(line) if x in ['.', '#']])
    edges.append((left_end, right_end))
    blocks.append([i for i, x in enumerate(line) if x in ['#']])
    if y == 0:
        pos = (left_end, y)

commands = [int(_) if _.isnumeric() else _ for _ in re.findall(r'(\d+|L|R)', _input.splitlines()[-1])]

for c in commands:
    if isinstance(c, int):
        for step in range(c):
            x, y = pos[0] + direction.current[0], pos[1] + direction.current[1]
            if direction.current in (Direction.DOWN, Direction.UP):
                min_y = min([i for i, l in enumerate(grid_lines) if len(l) > x and l[x] in ['.', '#']])
                max_y = max([i for i, l in enumerate(grid_lines) if len(l) > x and l[x] in ['.', '#']])
                if y < min_y:
                    y = max_y
                    #print(f"Wrap to bottom {max_y}")
                elif y > max_y:
                    y = min_y
                    #print(f"Wrap to top {min_y}")
            else:
                l, r = edges[y]
                if x < l:
                    x = r
                    #print(f"Wrap to r {r}")
                elif x > r:
                    x = l
                    #print(f"Wrap to l {l}")
            if x in blocks[y]:
                # Hit Block
                #print(f"Hit Block @ {x},{y}")
                break
            else:
                pos = x, y
                #print(f"Moved to {pos}")
    else:
        direction.turn(c)
        #print(f"Turned {c} to {direction.current}")

print("Part 1: ", ((pos[1] + 1) * 1000) + ((pos[0] + 1) * 4) + direction.value)
print("Part 2: ", )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
