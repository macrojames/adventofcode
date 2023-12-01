#!/usr/bin/env python3
from copy import deepcopy
import os
import time
from util import read_input_lines, read_input_raw
import re
from math import prod
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_raw(day, SAMPLE)


class Monkey():
    def __init__(self, no, items, operation, div_test, true_monkey, false_monkey) -> None:
        self.no = no
        self.items = items
        self.operation = operation
        self.div_test = div_test
        self.targets = [false_monkey, true_monkey]
        self.item_in_hand = None
        self.inspections = 0

    def __repr__(self) -> str:
        return f"<Monkey {self.no}: {self.items}, op: {self.operation}, div by {self.div_test}, inspections: {self.inspections}>"

    def new_relief(self, item, all_div_tests) ->int:
        return item % prod(all_div_tests)

    def inspect(self, relief = 1, all_div_tests=[]):
        self.inspections += 1
        item = self.items.pop(0)
        if relief == 1:
            item = self.operate(item)
            item = self.new_relief (item, all_div_tests)
        else:
            item = self.operate(item)
            item = item // relief
        
        self.item_in_hand = item

    def operate(self, old) -> int:
        new = self.operation(old)
        return new

    def test_and_throw(self) -> int:
        ret = self.targets[self.item_in_hand % self.div_test == 0], self.item_in_hand
        self.item_in_hand = None
        return ret

monkeys_original = []
all_div_tests = []
worry_level = 0

for block in _input.split("\n\n"):
    monkey_no = int(re.findall(r"\d+", block.splitlines()[0])[0])
    items = list(map(int, re.findall(r"\d+", block.splitlines()[1])))
    tmp_operation = block.splitlines()[2].split("= ")[1]
    operation = eval(f"lambda old: {tmp_operation}")
    div_test = int(re.findall(r"\d+", block.splitlines()[3])[0])
    true_monkey = int(re.findall(r"\d+", block.splitlines()[4])[0])
    false_monkey = int(re.findall(r"\d+", block.splitlines()[5])[0])
    monkeys_original.append(Monkey(monkey_no, items, operation,
                   div_test, true_monkey, false_monkey))
    all_div_tests.append(div_test)

for part, max_rounds in enumerate([20, 10000]):
    monkeys = deepcopy(monkeys_original)
    for rounds in range(max_rounds):
        for turn in range(len(monkeys)):
            while monkeys[turn].items:
                monkeys[turn].inspect(relief = 3 if part == 0 else 1, all_div_tests = all_div_tests)
                target, item = monkeys[turn].test_and_throw()
                monkeys[target].items.append(item)
    top_inspectors = sorted([_.inspections for _ in monkeys], reverse=True)
    print(f"Part {part + 1}: ", top_inspectors[0] * top_inspectors[1], monkeys)

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
