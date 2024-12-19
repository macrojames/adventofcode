#!/usr/bin/env python3
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

robot = None
walls = set()
boxes = set()
instructions = []
dirs = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}
max_r = 10000
max_c = 0

for r, line in enumerate(inputs):
    if line.count('#') < 2:
        max_r = min(max_r, r)
        # mode instructions!
        instructions.extend(list(line))
        continue
    for c, char in enumerate(line):
        if char == '@':
            robot = (r, c)
        elif char == '#':
            walls.add((r,c))
        elif char == 'O':
            boxes.add((r,c))
    max_c = c + 1

def part1(robot, boxes):
    for move in instructions:
        dr, dc = dirs[move]
        nr, nc = robot[0] + dr, robot[1] + dc

        if (nr, nc) in walls:
            continue
        
        if (nr, nc) in boxes:
            # find a free space
            n = 1
            while 0 <= (sr := nr + (n*dr)) < max_r and 0 <= (sc := nc + (n*dc)) < max_c and (sr, sc) not in walls:
                if (sr, sc) not in boxes:
                    # robot -> box, box -> free
                    robot = (nr, nc)
                    boxes.remove((nr, nc))
                    boxes.add((sr, sc))
                    break
                n += 1
        else:
            robot = (nr, nc)
    return sum([r*100+c for r,c in boxes])
         
class Box:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __repr__(self):
        return f"Box @ {self.r, self.c}"

    def is_hit(self, r, c):
        return self.r == r and (c in [self.c, self.c+1])
    
    def hit_char(self, r, c):
        if self.r == r and c == self.c: return '['
        if self.r == r and c == self.c + 1: return ']'
        return ''
    
    def move(self, dr, dc):
        self.r += dr
        self.c += dc

    @property
    def span(self):
        return [self.c, self.c + 1]

    @property
    def gps(self):
        return self.r * 100 + self.c


def part2():
    robot = None
    walls = set()
    boxes = set()
    max_r = 10000
    max_c = 0
    instructions = []
    def print_grid(robot, boxes):
        for r in range(max_r):
            for c in range(max_c):
                print("@" if (r,c) == robot else ('#' if (r,c) in walls else ([b.hit_char(r,c) for b in boxes if b.is_hit(r,c)] or ['.'])[0]) , end="")
            print()
        print()
    for r, line in enumerate(inputs):
        if line.count('#') < 2:
            max_r = min(max_r, r)
            # mode instructions!
            instructions.extend(list(line))
            continue
        new_line = line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
        for c, char in enumerate(new_line):
            if char == '@':
                robot = (r, c)
            elif char == '#':
                walls.add((r,c))
            elif char == '[':
                boxes.add(Box(r,c))
        max_c = c + 1
    print_grid(robot, boxes)

    for move in instructions:
        dr, dc = dirs[move]
        nr, nc = robot[0] + dr, robot[1] + dc

        if (nr, nc) in walls:
            #print_grid(robot, boxes)
            continue
        if not any(b.is_hit(nr, nc) for b in boxes):
            robot = (nr, nc)
            #print_grid(robot, boxes)
            continue

        if move in ['<', '>']: 
            n = 1
            hit_boxes = set()
            while 0 <= (sr := nr + (n*dr)) < max_r and \
                  0 <= (sc := nc + (n*dc)) < max_c and \
                    (sr, sc) not in walls:

                if hit := next((b for b in boxes if b.is_hit(sr, sc)), None):
                    hit_boxes.add(hit)
                else:
                    # not wall, not box -> empty?!
                    robot = (nr, nc)
                    for b in hit_boxes:
                        b.move(dr, dc)
                    break
                n += 1

        else:
            # TODO: row movement
            # any over top row hit wall? -> stop 
            n = 1
            first_box = [b for b in boxes if b.is_hit(nr, nc)][0]
            hit_boxes = set([first_box])
            impacted = set(first_box.span)
            row_hit_wall = False
            while impacted and not row_hit_wall:
                new_impacted = set()
                row = nr + (n*dr)
                for col in impacted.copy():
                    if (row, col) in walls:
                        row_hit_wall = True
                        break
                    else:
                        hit = next((b for b in boxes if b.is_hit(row, col)), None)
                        if hit:
                            hit_boxes.add(hit)
                            new_impacted |= set(hit.span)
                if row_hit_wall: break
                n += 1
                impacted = new_impacted
            else:
                # no break, means no wall
                # -> move all boxes
                for b in hit_boxes:
                    b.move(dr, dc)
                    robot = (nr, nc)
        #print_grid(robot, boxes)
    return sum([b.gps for b in boxes])

#print("Part 1: ", part1(robot, boxes))
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

