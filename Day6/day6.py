def part(fn):
    total = 0
    currentSet = set()
    newGroup = True
    for line in open('Day6/day6.txt').read().splitlines():
        if (line == ""):
            total += len(currentSet)
            currentSet = set()
            newGroup = True
        else:
            if (newGroup):
                currentSet = set(list(line))
                newGroup = False
            else:                
                currentSet = fn(currentSet, set(list(line)) )
    total += len(currentSet)
    return total

def part1():
    print(part(lambda x, y: x.union(y)))

def part2():
    print(part(lambda x, y: x.intersection(y)))

part1()     #6585
part2()     #3276
