#!/usr/bin/env python3
import os
import time
from parse import parse
from util import read_input_lines, read_input_raw
from functools import lru_cache

start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)
sensormap = [parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line).fixed for line in _input]
sensors = [(_[0], _[1]) for _ in sensormap]
beacons = [(_[2], _[3]) for _ in sensormap]


def union_ranges(ranges: list[tuple[int, int]]):
    b = []
    for begin, end in sorted(ranges):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b


def distance(x, y, other_x, other_y):
    return abs(other_x - x) + abs(other_y - y)

@lru_cache(maxsize=None)
def sensor_range(sensor):
    return distance(*sensor)


def coverage(sensor, row, window=None) -> tuple[int, int]:
    r = sensor_range(sensor)
    h = abs(sensor[1] - row)
    if h > r:
        return None, None
    x_min, x_max = sensor[0] - (r - h), sensor[0] + (r - h)
    if window is not None:
        x_min = max(x_min, WINDOW[0])
        x_max = min(x_max, WINDOW[1])
    return x_min, x_max


def count_ranges(ranges: list[tuple[int, int]], row_beacons: list[int]) -> int:
    x_min = min([_[0] for _ in ranges])
    x_max = max([_[1] for _ in ranges])
    return sum(map(lambda x: abs(x[1]-x[0]), union_ranges(ranges)))


ROW = 10 if SAMPLE else 2000000
coverage_ranges = list(filter(lambda x: x[0] is not None, [coverage(sensor, ROW) for sensor in sensormap]))
free = count_ranges(coverage_ranges, set([b[0] for b in beacons if b[1] == ROW]))

WINDOW = (0, 20) if SAMPLE else (0, 4000000)
for y in range(WINDOW[1] + 1):
    if y % 50000 == 0: print(f"Step y={y}  {round(y / WINDOW[1] * 100)} % Time elapsed: {round(time.time() - start_timer, 3)}s freq = {round(y / (time.time() - start_timer))}/s")
    coverages = (coverage(sensor, y, window=WINDOW) for sensor in sensormap)
    coverage_ranges = filter(lambda x: x[0] is not None, coverages)
    uni_range = union_ranges(coverage_ranges)
    #if len(uni_range) > 1:
    #    print(f"y: {y}", uni_range)
    #    distress_x = uni_range[0][0] + 1
    #    distress_y = y
    #    break
    if uni_range[0][0] != WINDOW[0] or uni_range[0][1] != WINDOW[1]:
        distress_x = uni_range[0][1] + 1
        distress_y = y
        print(f"y: {y}", )
        break

print("Part 1: ", free)
print("Part 2: ", distress_x * 4000000 + y)
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
