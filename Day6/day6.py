from functools import reduce

groups = open('Day6/day6.txt').read().split('\n\n')

def solve(fn):
    return sum(map(lambda group: len(reduce(lambda p1, p2 : fn(p1, p2), map(set, group.split('\n')))), groups))

print(f"Part 1 = {solve(lambda x, y: x | y)}")
print(f"Part 2 = {solve(lambda x, y: x & y)}")

# part1()     #6585
# part2()     #3276

# Short version!
# from functools import reduce
# print(sum(map(lambda group: len(reduce(lambda p1, p2 : p1 | p2, map(set, group.split('\n')))), open('Day6/day6.txt').read().split('\n\n'))))
# print(sum(map(lambda group: len(reduce(lambda p1, p2 : p1 & p2, map(set, group.split('\n')))), open('Day6/day6.txt').read().split('\n\n'))))