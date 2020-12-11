grid = open('Day11/day11.txt').read().splitlines()
rows = len(grid)
columns = len(grid[0])

def adjacent_seats(x, y, grid):
    #  abc
    #  dXe
    #  fgh 
    result = []
    #a
    if x > 0 and y > 0:
        result.append(grid[y-1][x-1])

    #b
    if y > 0:
        result.append(grid[y-1][x])

    #c
    if x + 1 < columns and y > 0:
        result.append(grid[y-1][x+1])

    #d
    if x > 0:
        result.append(grid[y][x-1])

    #e
    if x + 1 < columns:
        result.append(grid[y][x+1])

    #f
    if x > 0 and y + 1 < rows:
        result.append(grid[y+1][x-1])

    #g
    if y + 1 < rows:
        result.append(grid[y+1][x])

    #h
    if x + 1 < columns and y + 1 < rows:
        result.append(grid[y+1][x+1])
    return result


def visible_seats(x, y, grid):
    currentX  = x
    currentY  = y

    #  abc
    #  dXe
    #  fgh 
    result = []
    #a
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #b
    while y > 0:
        y -= 1        
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #c
    while x + 1 < columns and y > 0:
        x += 1
        y -= 1        
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #d
    while x > 0:
        x -= 1
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #e
    while x + 1 < columns:
        x += 1
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #f
    while x > 0 and y + 1 < rows:
        x -= 1
        y += 1        
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #g
    while y + 1 < rows:
        y += 1        
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    #h
    while x + 1 < columns and y + 1 < rows:
        x += 1
        y += 1        
        if grid[y][x] != '.':
            result.append(grid[y][x])
            break
    x = currentX
    y = currentY

    return result


def mutate_grid(seatsFunction, minOccupiedSeatCount, currentGrid):
    newGrid = []
    changed = False

    for r in range(0, rows):
        row = ""
        for c in range(0, columns):
            n = seatsFunction(c,r,currentGrid)
            if n.count('#') == 0 and currentGrid[r][c] == 'L':
                row += '#'
                changed = True
            elif currentGrid[r][c] == '#' and n.count('#') >= minOccupiedSeatCount:
                row += 'L'
                changed = True
            else:
                row += currentGrid[r][c]
        newGrid.append(row)
    return (newGrid, changed)

def part_one(grid):
    changed = True
    while changed:
        grid, changed = mutate_grid(adjacent_seats, 4, grid)        

    count = 0
    for row in grid:
        count += row.count('#')

    return count

def part_two(grid):
    changed = True

    while changed:
        grid, changed = mutate_grid(visible_seats, 5, grid)        

        count = 0
        for row in grid:
            count += row.count('#')        
        print(count)


    count = 0
    for row in grid:
        count += row.count('#')

    return count

print(part_two(grid))
#2329