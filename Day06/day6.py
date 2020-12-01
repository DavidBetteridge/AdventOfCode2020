import operator
from functools import reduce

groups = open('Day06/day6.txt').read().split('\n\n')

def solve(fn):
    return sum(map(lambda group: len(reduce(lambda p1, p2 : fn(p1, p2), map(set, group.split('\n')))), groups))

def part_one():
    return solve(operator.or_)

def part_two():
    return solve(operator.and_)

# Short version!
# from functools import reduce
# print(sum(map(lambda group: len(reduce(set.intersection, map(set, group.split('\n')))), open('Day6/day6.txt').read().split('\n\n'))))
# print(sum(map(lambda group: len(reduce(set.union, map(set, group.split('\n')))), open('Day6/day6.txt').read().split('\n\n'))))
