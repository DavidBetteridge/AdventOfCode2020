from copy import deepcopy

lines = open('Day17/day17.txt').read().splitlines()

def load_grid():
    grid = {}
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] == "#":
                grid[(0,x,y,0)] = True
    return grid

def is_alive(grid, w, x, y, z):        
    return (w,x,y,z) in grid and grid[(w,x,y,z)] == True

def count_active_neighbours(grid, w, x, y, z, wOffsetRange):
    count = 0
    for wOffset in wOffsetRange:
        for xOffset in [-1, 0, 1]:
            for yOffset in [-1, 0, 1]:
                for zOffset in [-1, 0, 1]:
                    if wOffset != 0 or xOffset != 0 or yOffset != 0 or zOffset != 0:
                        if is_alive(grid, w+wOffset, x+xOffset, y+yOffset, z+zOffset):
                            count += 1
    return count                                                

def solve(wOffsetRange):
    grid = load_grid()
    for _ in range(6):
        previous = deepcopy(grid)
        minW = min(grid, key = lambda t: t[0])[0]
        minX = min(grid, key = lambda t: t[1])[1]
        minY = min(grid, key = lambda t: t[2])[2]
        minZ = min(grid, key = lambda t: t[3])[3]
        maxW = max(grid, key = lambda t: t[0])[0]
        maxX = max(grid, key = lambda t: t[1])[1]
        maxY = max(grid, key = lambda t: t[2])[2]
        maxZ = max(grid, key = lambda t: t[3])[3]

        for w in range(minW - 1, maxW + 2):
            for x in range(minX - 1, maxX + 2):
                for y in range(minY - 1, maxY + 2):
                    for z in range(minZ - 1, maxZ + 2):
                        active_neighbours = count_active_neighbours(previous, w, x, y, z, wOffsetRange)

                        if is_alive(previous, w, x, y, z):
                            if active_neighbours != 2 and active_neighbours != 3:
                                grid[(w,x,y,z)] = False

                        else:
                            if active_neighbours == 3:
                                grid[(w,x,y,z)] = True

    print(sum([grid[k] for k in grid]))

solve([0])
solve([-1,0,1])

#1868