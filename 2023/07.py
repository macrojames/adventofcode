#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
from itertools import batched
from collections import Counter
from math import sqrt, ceil, floor, prod

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines('07', SAMPLE)


class Card():

    single_values = ['-1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] # With dummy for minimum rank = 1
    def __init__(self, carddef, bid):
        self.carddef = carddef
        self.cards = Counter(sorted(carddef, key=lambda x: Card.single_values.index(x)))
        self.cards_no_joker = Counter(sorted(carddef.replace('J', ''), key=lambda x: Card.single_values.index(x)))
        
        self.bid = int(bid)
        
    @property
    def value(self):
        val = 0
        for c, n in self.cards.items():
            if n > 1:
                val += 1000**n
        for i in range(0, 5):
            p = 4 - i
            val += Card.single_values.index(self.carddef[i]) * len(Card.single_values) ** p
        return val
    
    @property
    def value_with_joker(self):
        single_values_j = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'] 
        val = 0
        for i, (c, n) in enumerate(self.cards_no_joker.most_common()):
            if i == 0: # Add Jokers to worthiest
                n += self.cards.get('J', 0)
            if n > 1:
                val += 1000**n
        if val == 0 and self.cards.get('J', 0):
            assert self.cards.get('J', 0) == 5
            val += 1000**5

        for i in range(0, 5):
            p = 4 - i
            val += single_values_j.index(self.carddef[i]) * len(single_values_j) ** p
        return val


def part1():
    cards = [Card(_.split(" ")[0], _.split(" ")[1]) for _ in inputs]
    order = sorted([(_.value, _) for _ in cards], key=lambda x:x[0])
    points = 0
    for rank, c in enumerate(order):
        points += (rank+1) * c[1].bid
    return points
def part2():
    cards = [Card(_.split(" ")[0], _.split(" ")[1]) for _ in inputs]
    order = sorted([(_.value_with_joker, _) for _ in cards], key=lambda x:x[0])
    points = 0
    for rank, c in enumerate(order):
        points += (rank+1) * c[1].bid
    return points


print("Part 1: ", part1())
print("Part 2: ", part2())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
