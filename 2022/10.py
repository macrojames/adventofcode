#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

class CPU(object):
    def __init__(self, instructions):
        self.register = 1
        self.cycle = 0
        self.instructions = instructions
        self.triggers = [20, 60, 100, 140, 180, 220]
        self.signal_strength_sum = 0
        self.crt = [[] for _ in range(6)]

    def next_cycle(self):
        self.cycle += 1
        if self.cycle in self.triggers:
            self.signal_strength_sum += self.cycle * self.register
        self.draw()
    
    def draw(self):
        crt_position = (self.cycle - 1) % 40
        crt_line = (self.cycle - 1) // 40
        pixel = "#" if (self.register - 1) <= crt_position <= (self.register + 1) else "."
        self.crt[crt_line].append(pixel)
        
    def crt_print(self):
        return "\n".join("".join(line) for line in self.crt)
    
    def run(self):
        for cmd in self.instructions:
            if cmd == 'noop':
                self.next_cycle()
            elif cmd.startswith('addx'):
                self.next_cycle()
                self.next_cycle()
                self.register += int(cmd.split(" ")[1])
        return self.signal_strength_sum



tube =  CPU(_input)
print("Part 1: ", tube.run())
print("Part 2: ")
print(tube.crt_print())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
