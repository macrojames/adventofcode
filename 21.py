#!/usr/bin/env python3
import os
import time
from parse import parse
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

def monkey(part=1):
    public = {}
    operations = {}
    for line in _input:
        if res := parse("{:4l}: {:d}", line):
            public[res.fixed[0]] = res.fixed[1]
        elif res := parse("{:4l}: {:4l} {} {:4l}", line):
            operations[res.fixed[0]] = ([*res.fixed[1:]])

    if part == 2:
        del(public['humn'])
        operations['root'][1] = '='
    while operations:
        solvable = [k for k, v in operations.items() if v[0] in public and v[2] in public]
        if not solvable:
            human(operations, public)
            return public
        for var in solvable:
            l, op, r = operations[var]
        # autopep8: off
            if op == '+': number = public[l] + public[r] 
            elif op == '-': number = public[l] - public[r] 
            elif op == '*': number = public[l] * public[r] 
            elif op == '/': number = public[l] // public[r]
        # autopep8: on
            public[var] = number
            del(operations[var])
    return public

def human(operations, public):
    for var in operations:
        if operations[var][0] in public: operations[var][0] = public[operations[var][0]]
        if operations[var][2] in public: operations[var][2] = public[operations[var][2]]
        # depending on humans
    resolve_var = [operations['root'][0]]
    result = operations['root'][2]
    while resolve_var and resolve_var != ['humn']:
        node = resolve_var.pop()
        if isinstance(operations[node][2], int):
            var, op, value = operations[node]
        # autopep8: off
            if op == '+': result -= value                      #  12 = x + 5
            elif op == '-': result += value
            elif op == '*': result //= value                   #  12 = x * 4
            elif op == '/': result *= value                    #  12 = x / 4
        else:
            value, op, var = operations[node]
            if op == '+': result -= value                      #  12 = 5 + x
            elif op == '-': result = value - result            #  12 = 5 - x --> x = 5 - 12
            elif op == '*': result //= value                    #  12 = 4 * x 
            elif op == '/': result = value // result           #  12 = 4 / x --> 12/4 = x
        # autopep8: on
        resolve_var.append(var)
    public['humn'] = result


part1 = monkey()
print("Part 1: ", part1['root'])
part2 = monkey(2)
print("Part 2: ", part2['humn'])
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
