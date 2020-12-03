lines = open('Day3/day3.txt').read().splitlines()

def countTrees(stepX, stepY):
    currentX = 0
    currentY = 0
    treesFound = 0
    forestHeight = len(lines)
    forestWidth = len(lines[0])

    while (currentY + 1 < forestHeight):
        currentX = (currentX + stepX) % forestWidth
        currentY = currentY + stepY

        symbol = lines[currentY][currentX]

        if (symbol == '#'):
            treesFound = treesFound + 1

    return treesFound

print(countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2))