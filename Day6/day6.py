from functools import reduce

groups = open('Day6/day6.txt').read().split('\n\n')

def solve(fn):
    def solve_group(group):
        people = map(set, group.split('\n'))
        return len(reduce(lambda p1, p2 : fn(p1, p2), people))

    return sum(map(solve_group, groups))

def part1():
    print(solve(lambda x, y: x | y))

def part2():
    print(solve(lambda x, y: x & y))

part1()     #6585
part2()     #3276
