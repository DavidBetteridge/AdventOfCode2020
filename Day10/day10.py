lines = sorted(map(int,open('Day10/day10.txt').read().splitlines()))

def part_one():
    oneCount=0
    threeCount=1

    if lines[0] == 1:
        oneCount += 1

    if lines[0] == 3:
        threeCount += 1

    for i in range(0, len(lines) - 1):
        if lines[i + 1] - lines[i] == 1:
            oneCount += 1
        if lines[i + 1] - lines[i] == 3:
            threeCount += 1

    zip(lines, lines)

    return oneCount * threeCount
    #2170
    #zip might be better

def part_two():
    lines.insert(0,0)
    lines.append(lines[len(lines)-1] + 3)

    numberOfRoots = {}
    numberOfRoots[len(lines)-1] = 1

    for i in range(len(lines)-2, -1, -1):
        numberOfRoots[i] = 0
        index = i+1
        while index < len(lines) and (lines[index] - lines[i]) <= 3:
            numberOfRoots[i] += numberOfRoots[index]
            index = index + 1

    return numberOfRoots[0]

print(part_one())    
print(part_two())    
