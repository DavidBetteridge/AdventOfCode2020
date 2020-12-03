lines = open('Day3/day3.txt').read().splitlines()

currentX = 0
currentY = 0
stepX = 3
stepY = 1
treesFound = 0
forestHeight = len(lines)
forestWidth = len(lines[0])

while (currentY + 1 < forestHeight):
    currentX = (currentX + stepX) % forestWidth
    currentY = currentY + stepY

    symbol = lines[currentY][currentX]

    if (symbol == '#'):
        treesFound = treesFound + 1


print(treesFound)