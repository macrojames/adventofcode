#!/usr/bin/env python3
import time
import re
from util import read_input_lines
from functools import cache

start_timer = time.time()

SAMPLE = False
DEBUG = False

inputs = read_input_lines('12', SAMPLE)
sources = [tuple(l.split(" ")[0]) for l in inputs]
mutations = [tuple([int(x) for x in l.split(" ")[1].split(",")]) for l in inputs]

wc = set(['#', '?'])

@cache
def mutate(src, mutations):
    # tuples are hashable -> cachable
    src = list(src)
    mutations = list(mutations)

    if DEBUG: print(f"Analyzing {"".join(src)} for {mutations}")
    solutions = []
    if not mutations or not src:
        return solutions
    current_mut = mutations[0]
    if len(mutations) > 1:
        rest_sum = sum(mutations[1:]) + current_mut - 1
    else:
        rest_sum = current_mut - 1

    for i in range(len(src) - rest_sum):
        if src[i] == '.':
            continue

        if not set(src[i:i+current_mut]) - wc \
           and (i+current_mut >= len(src) or src[i+current_mut] in ['.', '?']) \
           and src[:i].count('#') == 0:
            prefix = f"{'.' * i}{'#' * current_mut}"
            trail_length = len(src) - len(prefix)
            if len(mutations) == 1 and src[i + current_mut + 1:].count('#') == 0:
                prefix += '.' * trail_length if len(src) > i + current_mut else ''
            elif len(mutations) == 1 and src[i + current_mut + 1:].count('#') > 0:
                continue # Error: trailing '#'
            else:
                prefix += '.'
            if DEBUG: print(f"Found Prefix in {"".join(src)} having {current_mut}: {prefix}")
            if len(mutations) > 1:
                suffixes = mutate(tuple(src[i + current_mut + 1:]), mutations=tuple(mutations[1:]))
                for suffix in suffixes:
                    solutions.append(f"{prefix}{suffix}")
            else:
                solutions.append(prefix)

    return solutions


def part1():
    su = 0

    for i, (s, m) in enumerate(zip(sources, mutations)):
        if DEBUG and i % 10 == 0: print(f"{i + 1} of {len(sources)}: Current Sum: {su:10}", end=' + ')
        l = len(mutate(s, m))
        su += l
        if DEBUG and i % 10 == 0: print(f"{l:7}")
    return su

def part2():
    su = 0

    for i, (s, m) in enumerate(zip(sources, mutations)):
        if i % 10 == 0: print(f"{i + 1} of {len(sources)}: Current Sum: {su:10}", end=' + ')
        #print((s + ['?']) * 5, m * 5)
        s = list(s)
        fi = s + ['?'] + s + ['?'] + s + ['?'] + s + ['?'] + s # Fuck it, sonst hängt hinten ein ? dran.
        l = len(mutate(tuple(fi), m * 5))
        su += l
        if i % 10 == 0: print(f"{l:7}")
    return su


if SAMPLE and DEBUG:
    assert len(mutate(sources[0], mutations[0])) == 1
    assert len(mutate(sources[1], mutations[1])) == 4
    assert len(mutate(sources[2], mutations[2])) == 1
    assert len(mutate(sources[3], mutations[3])) == 1
    assert len(mutate(sources[4], mutations[4])) == 4
    assert len(mutate(sources[5], mutations[5])) == 10


print("Part 1:", part1())
#print("Part 2:", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
