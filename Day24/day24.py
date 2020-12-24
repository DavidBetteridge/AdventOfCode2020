def part_one():
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
        
        tile = (x, y)
        if tile not in tiles:
            tiles[tile] = True
        else:
            tiles[tile] = not tiles[tile]

    return sum([1 for tile in tiles if tiles[tile]])

def part_two():
    pass

print(part_one())

