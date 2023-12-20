#!/usr/bin/env python3
from functools import cache
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

CONJUNCTION, FLIPFLOP, BROADCAST, OUTPUT = '&', '%', 'b', 'o'
LOW, HIGH = -1, 1

gates = {}

class Gate:
    def __init__(self, definition):
        name, outputs =  line.split(" -> ")
        self.outputs = outputs.split(", ")
        if not self.outputs: self.type = OUTPUT
        else: self.type = name[0] if name[0] in [CONJUNCTION, FLIPFLOP] else BROADCAST
        self.state = []
        self.inputs = {}
        self.out = -1
        self.name = name[1:] if self.type in [CONJUNCTION, FLIPFLOP] else name

    def __repr__(self):
        return f"Gate<{self.name}>: {self.out}  ({self.state}) -> {self.outputs}"

    def receive_pulse(self, pulse, source=None):
        if self.type == BROADCAST:
            self.out = pulse
            return True
        if self.type == FLIPFLOP:
            if pulse == LOW:
                self.out = self.out * pulse
                return True
        if self.type == CONJUNCTION:
            self.inputs[source] = pulse
            old = self.out
            self.out = LOW if all(HIGH==_ for _ in self.inputs.values()) else HIGH
            return not(self.out == old) # Only Updates        
        return False
    
    def pass_pulse(self):
        for out in self.outputs:
            gates[out].receive_pulse(pulse=self.out, source=self.name)


def send_pulse(target, pulse):
    pass


for line in inputs:
    a = Gate(line)
    gates[a.name] = a
for a in gates:
    if gates[a].type == CONJUNCTION:
        for out in gates[a].outputs:
            gates[out].inputs[a] = -1

def part1():
    gates['broadcaster'].receive_pulse(LOW)
    print(gates)
    gates['broadcaster'].pass_pulse()
    print(gates)
    return 

print("Part 1: ", part1())
#print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

