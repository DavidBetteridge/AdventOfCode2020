def part1():
    total = 0
    currentSet = set()
    for line in open('Day6/day6.txt').read().splitlines():
        if (line == ""):
            total += len(currentSet)
            currentSet = set()
        else:
            if (len(currentSet) == 0):
                currentSet = set(list(line))
            else:                
                currentSet = currentSet.union(set(list(line)))
    total += len(currentSet)

    print(total)

def part2():
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
                currentSet = currentSet.intersection(set(list(line)))
    total += len(currentSet)

    print(total)


part1()     #6585
part2()     #3323 too high