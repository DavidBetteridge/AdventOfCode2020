import time
import cProfile

def time_it(what):
    def decorator(func):
        def wrapper():
            tic = time.perf_counter()
            result = func()
            toc = time.perf_counter()
            print(f"Solved {what} in {toc - tic:0.4f} seconds")   
            return result
        return wrapper
    return decorator  

def layout_tiles():
    tiles = {}
    lines = open('C:/personal/AdventOfCode2020/Day24/day24.txt').read().splitlines()
    for line in lines:
        x = 4000
        y = 4000
        index = 0

        while index < len(line):

            if (index + 1) < len(line) and line[index] in ['n','s'] and line[index + 1] in ['e','w']:
                move = line[index:index+2]
                index += 2
            else:
                move = line[index]
                index += 1         

            if move == 'e':
                x += 1
            elif move == 'w':
                x -= 1
            elif move == 'nw':
                y += 1
            elif move == 'ne':
                x += 1
                y += 1
            elif move == 'sw':
                x -= 1
                y -= 1
            elif move == 'se':
                y -= 1
            else:
                print(f'Unknown move {move}')
        
        tile = (x << 16) | y
        if tile not in tiles:
            tiles[tile] = True
        else:
            tiles[tile] = not tiles[tile]
    return set([tile for tile in tiles if tiles[tile]])
    
@time_it("Part One")
def part_one():
    tiles = layout_tiles()
    return len(tiles)


@time_it("Part Two")
def part_two():
    tiles = layout_tiles()
    offsetsToCheck = [(0,0), (1,0), (-1,0), (0,1), (1,1), (0,-1), (-1,-1)]
    neighboursToCount = [(1,0), (-1,0), (0,1), (1,1), (0,-1), (-1,-1)]

    for _ in range(100):
        newTiles = set()
        checked = set()
        for blackTile in tiles:
            x = blackTile >> 16
            y = blackTile & 65535

            for offsetToCheck in offsetsToCheck:
                x1, y1 = x+offsetToCheck[0],y+offsetToCheck[1]
                key = (x1 << 16) | y1
                if not key in checked: 
                    checked.add(key)
                    count = 0
                    for neighbourToCount in neighboursToCount:
                        key1 = ((x1+neighbourToCount[0]) << 16) | (y1+neighbourToCount[1])
                        if key1 in tiles:
                            count+=1                

                    isCurrentlyBlack = key in tiles

                    if isCurrentlyBlack and (count == 0 or count > 2):
                        pass
                    elif not isCurrentlyBlack and (count == 2):
                        newTiles.add(key)
                    elif isCurrentlyBlack:
                        newTiles.add(key)

        tiles = newTiles
    return len(tiles)


print(part_one())  #277 Solved Part One in 0.0117 seconds
print(part_two())  #3531 Solved Part Two in 2.0459 seconds

# cProfile.run('part_two()')