from copy import deepcopy

lines = open('Day17/day17.txt').read().splitlines()

grid = {}
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[y][x] == "#":
            grid[(x,y,0)] = True

def count_active_neighbours(grid, x, y, z):
    count = 0
    for xOffset in [-1, 0, 1]:
        for yOffset in [-1, 0, 1]:
            for zOffset in [-1, 0, 1]:
                if xOffset != 0 or yOffset != 0 or zOffset != 0:
                    if (x+xOffset,y+yOffset,z+zOffset) in grid and grid[(x+xOffset,y+yOffset,z+zOffset)] == True:
                        count += 1
    return count                                                

def display(grid, x, y, z):
    if is_alive(grid, x, y, z):
        return "#"
    else:
        return "."

def displayGrid(grid):
    minX = min(grid, key = lambda t: t[0])[0]
    minY = min(grid, key = lambda t: t[1])[1]
    minZ = min(grid, key = lambda t: t[2])[2]
    maxX = max(grid, key = lambda t: t[0])[0]
    maxY = max(grid, key = lambda t: t[1])[1]
    maxZ = max(grid, key = lambda t: t[2])[2]
        
    for z in range(minZ, maxZ+1):
        print(f"z {z}")
        for y in range(minY, maxY+1):
            row = ""
            for x in range(minX, maxX+1):
                row = row + display(grid, x, y, z)                           
            print(row)                
    print("")      

def is_alive(grid, x, y, z):        
    return (x,y,z) in grid and grid[(x,y,z)] == True




for cycle in range(6):
    previous = deepcopy(grid)
    minX = min(grid, key = lambda t: t[0])[0]
    minY = min(grid, key = lambda t: t[1])[1]
    minZ = min(grid, key = lambda t: t[2])[2]
    maxX = max(grid, key = lambda t: t[0])[0]
    maxY = max(grid, key = lambda t: t[1])[1]
    maxZ = max(grid, key = lambda t: t[2])[2]

    for x in range(minX - 1, maxX + 2):
        for y in range(minY - 1, maxY + 2):
            for z in range(minZ - 1, maxZ + 2):
                active_neighbours = count_active_neighbours(previous, x, y, z)

                if is_alive(previous, x, y, z):
                    if active_neighbours == 2 or active_neighbours == 3:
                        grid[(x,y,z)] = True
                    else:
                        grid[(x,y,z)] = False

                else:
                    if active_neighbours == 3:
                        grid[(x,y,z)] = True

    count = 0
    for k in grid:
        if grid[k]:
            count += 1

    print(f"Cycle: {cycle + 1}")
    print(count)
  #  displayGrid(grid)              

#117 too low
#406 too high