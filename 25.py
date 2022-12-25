#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

import string
digs = '012=-'


def int2snafu(x, base=5) -> str:
    digits = []
    while x:
        digits.append(digs[x % base])
        carry = x % base > 2
        x = (x // base) + carry
    digits.reverse()
    return ''.join(digits)

def snafu2int(x, base=5) -> int:
    carry, value = 0, 0
    for i, char in enumerate(reversed(x)):
        num = digs.find(char)
        value = value + (num - carry) * 5 ** i
        carry = num > 2
    return value

#for x in [1,2,3,4,5,6,7,8,2022,314159265  ]:
#    print(f"{x} {int2snafu(int(x))} <-> {snafu2int(int2snafu(int(x)))}\n")

print("Part 1: ", int2snafu(sum(map(snafu2int, _input))))
print("Part 2: ", )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
