#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
import re
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")


class CPU(object):
    def __init__(self, register=[0, 0, 0]):
        self.register = [int(_) for _ in register]
        self.cycle = 0
        self.ip = 0
        self.output = []

    def get_combo(self, combo_operand):
        if combo_operand <= 3: return combo_operand
        elif combo_operand <= 6: return self.register[combo_operand-4]
        return -1

    def op_0(self, param):
        self.register[0] = int(self.register[0] // 2**self.get_combo(param))

    def op_1(self, param):
        self.register[1] = self.register[1] ^ param

    def op_2(self, param):
        self.register[1] = self.get_combo(param) % 8

    def op_3(self, param):
        if self.register[0] == 0: return
        self.ip = param - 2 

    def op_4(self, param):
        self.register[1] = self.register[1] ^ self.register[2]

    def op_5(self, param):
        self.output.append(str(self.get_combo(param) % 8))
        #print(f"Output: {self.get_combo(param) % 8:>12}")

    def op_6(self, param):
        self.register[1] = int(self.register[0] // 2**self.get_combo(param))

    def op_7(self, param):
        self.register[2] = int(self.register[0] // 2**self.get_combo(param))
   
    def run(self, instructions):
        self.output = []
        while self.ip < len(instructions):
            #print(f"{bin(self.register[0]):>46} {bin(self.register[1]):>46} {bin(self.register[2]):>46}")
            op = instructions[self.ip]
            param = int(instructions[self.ip + 1])
            getattr(self, f"op_{op}")(param)
            self.ip += 2

        return ",".join(self.output)


def part1():
    regs = list(re.match(r"Register A: (\d+)Register B: (\d+)Register C: (\d+)", "".join(inputs[:3])).groups())
    instructions = inputs[4].replace("Program: ", "").split(",")
    cpu = CPU(register=regs)
    return cpu.run(instructions)

print("Part 1: ", part1())
print(inputs[4])
def pretty():
    s = inputs[4].replace("Program: ", "").split(",")
    i = 0
    while i < len(s):
        s[i] = " " + ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"][int(s[i])] + ":"
        i += 2
    return "".join(s)
print(pretty())
#print("Part 2: ", part2())


instructions = inputs[4].replace("Program: ", "").split(",")
i = 0
for bit in range(16, -1, -2):
    for block in range(8**5): ### override previous if needed
        num = block*(8**bit)
        temp = CPU([i + num, 0, 0]).run(instructions)
        temp = temp.split(",")
        if temp[bit:] == instructions[bit:]:
            #print(f"{oct(i + num)} matched  {temp}")
            i += num
            break
print(f"Part 2: {i}")
print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

