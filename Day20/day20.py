import math

class Tile:
    def __init__(self, tileId):
        self.TileId = tileId
        self.Lines = []

    def rotate(self):
        self.Lines = list(zip(*self.Lines[::-1]))

    def flip_h(self):
        self.Lines = [ l[::-1] for l in self.Lines]

    def flip_v(self):
        self.Lines = self.Lines[::-1]

    def __repr__(self):
        return str(self.TileId)

    def __str__(self):
        return f"TileId : {self.TileId} {self.Lines}"

    def top_border(self):
        return ''.join(self.Lines[0])

    def bottom_border(self):
        return ''.join(self.Lines[-1])

    def left_border(self):
        result = ""
        for l in self.Lines:
            result += l[0]
        return ''.join(result)

    def right_border(self):
        result = ""
        for l in self.Lines:
            result += l[-1]
        return ''.join(result)

    def all_borders(self):
        return set([ self.top_border(), self.top_border()[::-1], 
                 self.bottom_border(), self.bottom_border()[::-1],
                 self.left_border(), self.left_border()[::-1],
                 self.right_border(), self.right_border()[::-1] 
               ])

    def remove_border(self):
        self.Lines = [ l[1:-1]  for l in self.Lines[1:-1] ]

def read_file():
    lines =  open('Day20/day20.txt').read().splitlines()

    tiles = {}
    for i in range(0, len(lines), 12):

        tileId = int(lines[i].replace("Tile ", "").replace(":", ""))
        tile = Tile(tileId)

        for r in range(1, 11):
            tile.Lines.append(lines[i + r])

        tiles[tileId] = tile
    return tiles        

def find_matches(tiles, tile, edge):
    result = []
    for otherTile in tiles.values():
        if otherTile.TileId != tile.TileId:
            if edge in otherTile.all_borders():
                result.append(otherTile.TileId)
    return result

def find_top_left_corner(tiles):
    for tile in tiles.values():
        if len(find_matches(tiles, tile, tile.top_border())) == 0 and len(find_matches(tiles, tile, tile.left_border())) == 0:
            return tile
    return None

def find_match_left_edge(tiles, edgeToMatch):
    for tileId in tiles:
        tile = tiles[tileId]
        for _ in range(4):
            if tile.left_border() == edgeToMatch:
                return tile
            tile.rotate()        
        tile.flip_h()
        for _ in range(4):
            if tile.left_border() == edgeToMatch:
                return tile
            tile.rotate()        

    return None

def find_match_top_edge(tiles, edgeToMatch):
    for tileId in tiles:
        tile = tiles[tileId]
        for _ in range(5):
            if tile.top_border() == edgeToMatch:
                return tile

            tile.flip_v()
            if tile.top_border() == edgeToMatch: return tile
            tile.flip_v()

            tile.rotate()        
        
    return None    

def complete_row(row, gridSize, remainingTiles):
    for i in range(0, gridSize - 1):
        edge_to_match = row[i].right_border()
        nextTile = find_match_left_edge(remainingTiles, edge_to_match)
        row.append(nextTile)
        remainingTiles.pop(nextTile.TileId, None)

def new_row(remainingTiles, grid):
    edge_to_match = grid[-1][0].bottom_border()
    nextTile = find_match_top_edge(remainingTiles, edge_to_match)
    row = [nextTile]
    grid.append(row)
    remainingTiles.pop(nextTile.TileId, None)            
    return row

def remove_all_borders(grid):
    for row in grid:
        for cell in row:
            cell.remove_border()

def combine_tiles(grid, gridSize):
    image = []
    for rowNumber in range(gridSize):
        for y in range(8):
            row = ""
            for columnNumber in range(gridSize):
                row += ''.join(grid[rowNumber][columnNumber].Lines[y])
            
            image.append(row)

    return image

def check_for_monster(image, topLineNumber):

    topLine = ''.join(image[topLineNumber])
    middleLine = ''.join(image[topLineNumber + 1])
    bottomLine = ''.join(image[topLineNumber + 2])

    offset = 0
    while offset + 20 < len(topLine):
        if middleLine[offset] == '#' and middleLine[offset + 5: offset + 7] == '##' and middleLine[offset + 11: offset + 13] == '##' and middleLine[offset + 17: offset + 20] == '###':
            if topLine[offset+18] == '#':
                if bottomLine[offset+1] == '#' and bottomLine[offset+4] == '#' and bottomLine[offset+7] == '#' and bottomLine[offset+10] == '#' and bottomLine[offset+13] == '#' and bottomLine[offset+16] == '#':
                    return True     
        offset += 1

def count_monsters(image):
    topLineNumber = 0
    result = 0
    while topLineNumber < len(image) - 2:
        if check_for_monster(image, topLineNumber):
            result +=1
        topLineNumber += 1    
    return result

def arrange_tiles(tiles, gridSize):
    grid = []

    topLeft = find_top_left_corner(tiles)
    tiles.pop(topLeft.TileId, None)

    row = [topLeft]
    grid.append(row)
    complete_row(row, gridSize, tiles)

    for _ in range(gridSize - 1):
        row = new_row(tiles, grid)
        complete_row(row, gridSize, tiles)

    return grid

def find_monsters(image):
    for _ in range(5):
        count = count_monsters(image)
        if count != 0: return count
        image = list(zip(*image[::-1]))

    image = image[::-1]
    for _ in range(5):
        count = count_monsters(image)
        if count != 0: return count
        image = list(zip(*image[::-1]))        

def part_one():
    tiles = read_file()
    gridSize = int(math.sqrt(len(tiles)))
    grid = arrange_tiles(tiles, gridSize)

    return grid[0][0].TileId * grid[0][-1].TileId * grid[-1][0].TileId * grid[-1][-1].TileId

def part_two():
    tiles = read_file()
    gridSize = int(math.sqrt(len(tiles)))
    grid = arrange_tiles(tiles, gridSize)

    remove_all_borders(grid)
    image = combine_tiles(grid, gridSize)

    monsterCount = find_monsters(image)

    result = sum([line.count('#') for line in image]) - (monsterCount * 15)
    return result 

print(part_one())    
print(part_two())    