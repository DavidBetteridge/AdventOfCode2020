from numpy import prod

lines = open('Day03/day3.txt').read().splitlines()
forestHeight = len(lines)
forestWidth = len(lines[0])

def countTrees(step):
    stepX, stepY = step
    currentX = 0
    currentY = 0
    treesFound = 0

    while (currentY + 1 < forestHeight):
        currentX = (currentX + stepX) % forestWidth
        currentY = currentY + stepY

        symbol = lines[currentY][currentX]

        if (symbol == '#'):
            treesFound = treesFound + 1

    return treesFound

def part_one():
    return countTrees((3,1))

def part_two():
    slopes = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
    return prod(list(map(countTrees, slopes)))