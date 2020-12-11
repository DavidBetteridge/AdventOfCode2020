grid = open('Day11/day11.txt').read().splitlines()
rows = len(grid)
columns = len(grid[0])

def neighbours(x, y, grid):
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


def mutate_grid(currentGrid):
    newGrid = []
    changed = False

    for r in range(0, rows):
        row = ""
        for c in range(0, columns):
            n = neighbours(c,r,currentGrid)
            if n.count('#') == 0 and currentGrid[r][c] == 'L':
                row += '#'
                changed = True
            elif currentGrid[r][c] == '#' and n.count('#') >= 4:
                row += 'L'
                changed = True
            else:
                row += currentGrid[r][c]
        newGrid.append(row)
    return (newGrid, changed)

def part_one():
    changed = True
    while changed:
        grid, changed = mutate_grid(grid)        

    count = 0
    for row in grid:
        count += row.count('#')

    return count

#2329