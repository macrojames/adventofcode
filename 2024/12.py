#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines, arr2d_get_near_idx
from collections import defaultdict, Counter
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

def parts():
    def bfs(node):
        visited = set()  # List for visited nodes.
        perimeter = 0
        queue = []  # Initialize a queue
        visited.add(node)
        queue.append(node)

        while queue:
            m = queue.pop(0)
            neighbors = [(m[0] + dr, m[1] + dc) for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr >= len(inputs) or nc >= len(inputs[0]):
                    # Randfeld -> perimeter + 1 und kein visit!
                    perimeter += 1
                elif inputs[nr][nc] != inputs[r][c]:
                    # Nachbar nicht gleich -> perimeter + 1 und kein visit!
                    perimeter += 1
                elif (nr, nc) not in visited: 
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return visited, perimeter

    already = set()
    s = 0
    p2 = 0
    for r, line in enumerate(inputs):
        for c, plant in enumerate(line):
            if (r,c) not in already:
                area, perimeter = bfs((r,c))
                #print(f"{len(area)} * {perimeter} = {len(area)*perimeter}")
                already |= area
                s += len(area)*perimeter
                p2 += (len(area) * (x:=count_polygon(area)))
                #print(f"{len(area)} * {x} = {len(area)*x}")
    return s, p2

def count_polygon(area):
    def check(edge):
        er, ec = edge
        return  ((er-.5, ec-.5) in area and (er+.5, ec+.5) in area) or \
                ((er-.5, ec+.5) in area and (er+.5, ec-.5) in area)
    
    edge_count = Counter([(r+dr, c+dc) for dr, dc in [(-.5, -.5), (.5, .5), (-.5, .5), (.5, -.5)] for r, c in area])
    regular = [_ for _, c in edge_count.items() if c in [1, 3]]
    diago = [test_edge for test_edge in [_ for _, c in edge_count.items() if c == 2] if check(test_edge)]
    sides = len(regular + 2 * diago)
    # Jede Ecke hat 2 Kanten, jede Kante zwei Ecken.
    # n = 4 vollständig umschlossen -> innen
    # n = 3 Ecke nach innen -> gut -> hat 2 Kanten
    # n = 2 Punkt zwischen genau 2 Pflanzen nicht diag -> keine Zusätzliche Kante, diag.. entspricht eigentlich 2 * 1Ecke
    # n = 1 Ecke ganz außen -> gut -> hat 2 Kanten

    '''
    ...   ...   ...   ...   ...   ...   ...   .#.             
    .#.   .#.   .##   .#.   ..#   .##   .##   .#.
    ...   .#.   ...   ..#   .#.   .#.   .##   .#.
                       ^
     4     4      4    8! aber vorher area abklären , ob umflossen.
    '''
    return sides

p1, p2 = parts()

print("Part 1: ", p1)
print("Part 2: ", p2)

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

