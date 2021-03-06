#!/usr/bin/python
# Floris Douw
# 2020
#
# AoC 2020 Day 23: Crab Cups

import sys
from numba import jit

input = '467528193'
rounds = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isnumeric() else 100


@jit
def play(initcups, ncups, rounds):
    # Use a list of integers, the value is the node (index) that is next
    input_size = len(initcups)
    cups = [0] * (ncups + 1)
    first = cur = initcups[0]
    for i in range(1, len(initcups)):
        cups[cur] = initcups[i]
        cur = cups[cur]
    for idx in range(input_size+1, ncups+1):
        cups[cur] = idx
        cur = idx
    cups[cur] = first  # Make the list loop around

    cur = first
    for _ in range(rounds):
        removed = (a := cups[cur], b := cups[a], c := cups[b])

        # Set destination, adjusting for removed cups
        dest = cur - 1 if cur > 1 else ncups
        while dest in removed:
            dest = dest - 1 if dest > 1 else ncups

        # Insert 'removed' cups after dest
        cups[cur] = cups[c]
        cups[c] = cups[dest]
        cups[dest] = a

        # Select next cup
        cur = cups[cur]

    return cups


allcups = play([*map(int, input)], 9, 100)
text = ''
cup = allcups[1]
while cup != 1:
    text += str(cup)
    cup = allcups[cup]
print(f'Part 1: {text}')

allcups = play([*map(int, input)], 1000000, 10000000)
cup = allcups[1]
print(f'Part 2: {cup * allcups[cup]}')