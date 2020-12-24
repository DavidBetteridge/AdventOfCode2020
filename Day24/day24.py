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
    return tiles
    

def part_one():
    tiles = layout_tiles()
    return sum([1 for tile in tiles if tiles[tile]])

def part_two():
    tiles = layout_tiles()

    for day in range(100):

        minX = min([tile[0] for tile in tiles])
        maxX = max([tile[0] for tile in tiles])
        minY = min([tile[1] for tile in tiles])
        maxY = max([tile[1] for tile in tiles])
        minZ = min([tile[2] for tile in tiles])
        maxZ = max([tile[2] for tile in tiles])

        newTiles = {}

        for x in range(minX-2,maxX+2):
            for y in range(minY-2,maxY+2):
                for z in range(minZ-2,maxZ+2):
                    count = 0
                    if (x+1,y-1,z) in tiles and tiles[(x+1,y-1,z)]:  #e
                        count+=1
                    if (x-1,y+1,z) in tiles and tiles[(x-1,y+1,z)]:  #w
                        count+=1
                    if (x,y+1,z-1) in tiles and tiles[(x,y+1,z-1)]:  #nw
                        count+=1
                    if (x+1,y,z-1) in tiles and tiles[(x+1,y,z-1)]:  #ne
                        count+=1
                    if (x,y-1,z+1) in tiles and tiles[(x,y-1,z+1)]:  #se
                        count+=1                    
                    if (x-1,y,z+1) in tiles and tiles[(x-1,y,z+1)]:  #sw
                        count+=1    

                    isCurrentlyBlack = (x,y,z) in tiles and tiles[(x,y,z)]

                    if isCurrentlyBlack and (count == 0 or count > 2):
                        pass
                    elif not isCurrentlyBlack and (count == 2):
                        newTiles[(x,y,z)] = True            
                    elif isCurrentlyBlack:
                        newTiles[(x,y,z)] = True 
        tiles = newTiles
        print(day+1, sum([1 for tile in tiles if tiles[tile]]))
    return sum([1 for tile in tiles if tiles[tile]])


print(part_one())
print(part_two())

