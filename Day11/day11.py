import sys, pygame, colorsys

DIRECTIONS = [ (-1,-1), (0,-1), (1,-1),
               (-1, 0),         (1, 0),
               (-1, 1), (0, 1), (1, 1) ]

grid = open('Day11/day11.txt').read().splitlines()
rows = len(grid)
columns = len(grid[0])

def valid_location(x, y):
    return 0 <= x < columns and 0 <= y < rows

def adjacent_seats(x, y, grid):
    return [ grid[y + direction[1]] [x + direction[0] ] for direction in DIRECTIONS if valid_location(x + direction[0], y + direction[1])]

def walk_in_direction(grid, x,y, xOffset, yOffset):
    while valid_location(x + xOffset, y + yOffset):
        x += xOffset
        y += yOffset
        if grid[y][x] != '.':
            return grid[y][x]
    return None

def visible_seats(x, y, grid):
    return [walk_in_direction(grid, x, y, *direction) for direction in DIRECTIONS]

def mutate_grid(seatsFunction, minOccupiedSeatCount, currentGrid):
    newGrid = []
    changed = False

    for r in range(0, rows):
        row = ""
        for c in range(0, columns):
            if currentGrid[r][c] == '.':
                row += '.'
            else:
                n = seatsFunction(c,r,currentGrid)
                if currentGrid[r][c] == 'L' and n.count('#') == 0:
                    row += '#'
                    changed = True
                elif currentGrid[r][c] == '#' and n.count('#') >= minOccupiedSeatCount:
                    row += 'L'
                    changed = True
                else:
                    row += currentGrid[r][c]
        newGrid.append(row)
    return (newGrid, changed)

def solver(seatsFunction, minOccupiedSeatCount):
    workingGrid = grid
    changed = True
    while changed:
        workingGrid, changed = mutate_grid(seatsFunction, minOccupiedSeatCount, workingGrid)        
    return sum(row.count('#') for row in workingGrid)

def part_one():
    return solver(adjacent_seats, 4)

def part_two():
    return solver(visible_seats, 5)

def main():
    pygame.init()
    cellSize = 10
    size = (columns * cellSize), (rows * cellSize)
    screen = pygame.display.set_mode(size)
    red = pygame.Color(255,0,0)    
    green = pygame.Color(0,255,0)  

    workingGrid = grid

    next_generation_event = pygame.USEREVENT + 1
    pygame.time.set_timer(next_generation_event, 100)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == next_generation_event:
                workingGrid, _ = mutate_grid(visible_seats, 5, workingGrid)   
    
                for c in range(0, columns):
                    for r in range(0, rows):
                        if workingGrid[r][c] == '#':                            
                            pygame.draw.rect(screen, green, (c*cellSize,r*cellSize,cellSize,cellSize))  

                        if workingGrid[r][c] == 'L':                            
                            pygame.draw.rect(screen, red, (c*cellSize,r*cellSize,cellSize,cellSize))  

                pygame.display.update()

if __name__ == '__main__':
    #main()    
    print(part_one())