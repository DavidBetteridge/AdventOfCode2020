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
    lines = open('Day24/day24.txt').read().splitlines()
    for line in lines:
        x = 0
        y = 0
        z = 0
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
                y -= 1
            elif move == 'w':
                x -= 1
                y += 1
            elif move == 'nw':
                z -= 1
                y += 1
            elif move == 'ne':
                x += 1
                z -= 1
            elif move == 'sw':
                x -= 1
                z += 1
            elif move == 'se':
                z += 1
                y -= 1
            else:
                print(f'Unknown move {move}')
        
        tile = (x, y, z)
        if tile not in tiles:
            tiles[tile] = True
        else:
            tiles[tile] = not tiles[tile]
    return set([tile for tile in tiles if tiles[tile]])
    
@time_it("Part One")
def part_one():
    tiles = layout_tiles()
    return len(tiles)

def next_generation(x, y, z, tiles, newTiles, checked):
    checked.add((x,y,z))

    count = 0
    if (x+1,y-1,z) in tiles:  #e
        count+=1
    if (x-1,y+1,z) in tiles:  #w
        count+=1
    if (x,y+1,z-1) in tiles:  #nw
        count+=1
    if (x+1,y,z-1) in tiles:  #ne
        count+=1
    if (x,y-1,z+1) in tiles:  #se
        count+=1                    
    if (x-1,y,z+1) in tiles:  #sw
        count+=1    

    isCurrentlyBlack = (x,y,z) in tiles

    if isCurrentlyBlack and (count == 0 or count > 2):
        pass
    elif not isCurrentlyBlack and (count == 2):
        newTiles.add((x,y,z))
    elif isCurrentlyBlack:
        newTiles.add((x,y,z))

@time_it("Part Two")
def part_two():
    tiles = layout_tiles()

    for _ in range(100):
        newTiles = set()
        checked = set()
        for blackTile in tiles:
            (x,y,z) = blackTile
            if not (x,y,z) in checked: next_generation(x,y,z, tiles, newTiles, checked)
            if not (x+1,y-1,z) in checked: next_generation(x+1,y-1,z, tiles, newTiles, checked)
            if not (x-1,y+1,z) in checked: next_generation(x-1,y+1,z, tiles, newTiles, checked)
            if not (x,y+1,z-1) in checked: next_generation(x,y+1,z-1, tiles, newTiles, checked)
            if not (x+1,y,z-1) in checked: next_generation(x+1,y,z-1, tiles, newTiles, checked)
            if not (x,y-1,z+1) in checked: next_generation(x,y-1,z+1, tiles, newTiles, checked)
            if not (x-1,y,z+1) in checked: next_generation(x-1,y,z+1, tiles, newTiles, checked)
        tiles = newTiles
    return len(tiles)


print(part_one())  #277 Solved Part One in 0.0117 seconds
print(part_two())  #3531 Solved Part Two in 2.5060 seconds

cProfile.run('part_two()')