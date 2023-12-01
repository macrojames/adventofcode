#!/usr/bin/env python3
import os
import time
import string
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

sum1, sum2 = 0, 0 
def get_prio(letter):
    return (string.ascii_lowercase + string.ascii_uppercase).index(letter) + 1

for i in range(len(_input) // 3):
    group = _input[i*3:i*3+3]
    for rucksack in group:
        left = rucksack[:len(rucksack)//2]
        right = rucksack[len(rucksack)//2:]
        
        double = set(left) & set(right)
        sum1 += sum(map(get_prio, double))
    
    badge = set(group[0]) & set(group[1]) & set(group[2])
    sum2 += sum(map(get_prio, badge))
    
print("Part 1: ", sum1)
print("Part 2: ", sum2)
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
