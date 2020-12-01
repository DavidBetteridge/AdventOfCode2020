import math

class Tile:
    def __init__(self, tileId):
        self.TileId = tileId
        self.Lines = []

    def rotate(self):
        self.Lines = list(zip(*self.Lines[::-1]))

    def flip_v(self):
        self.Lines = self.Lines[::-1]

    def __repr__(self):
        return str(self.TileId)

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

def edge_has_matches(tiles, tileId, edge):
    for otherTile in tiles.values():
        if otherTile.TileId != tileId:
            if edge in [ otherTile.top_border(), otherTile.top_border()[::-1], 
                         otherTile.bottom_border(), otherTile.bottom_border()[::-1],
                         otherTile.left_border(), otherTile.left_border()[::-1],
                         otherTile.right_border(), otherTile.right_border()[::-1] 
                       ]:
                return True
    return False

def find_top_left_corner(tiles):
    for tile in tiles.values():
        if not edge_has_matches(tiles, tile.TileId, tile.top_border()) and not edge_has_matches(tiles, tile.TileId, tile.left_border()):
            return tile
    return None

def find_matching_edge(tiles, edgeToMatch, fn):
    for tileId in tiles:
        tile = tiles[tileId]

        for _ in range(2):
            for _ in range(4):
                if fn(tile) == edgeToMatch:
                    return tile
                tile.rotate()        
            tile.flip_v()

    return None

def find_matching_left_edge(tiles, edgeToMatch):
    return find_matching_edge(tiles, edgeToMatch, lambda tile: tile.left_border() )

def find_matching_top_edge(tiles, edgeToMatch):
    return find_matching_edge(tiles, edgeToMatch, lambda tile: tile.top_border() )

def complete_row(row, gridSize, remainingTiles):
    for i in range(0, gridSize - 1):
        edge_to_match = row[i].right_border()
        nextTile = find_matching_left_edge(remainingTiles, edge_to_match)
        row.append(nextTile)
        remainingTiles.pop(nextTile.TileId, None)

def new_row(remainingTiles, grid):
    edge_to_match = grid[-1][0].bottom_border()
    nextTile = find_matching_top_edge(remainingTiles, edge_to_match)
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

def pattern_matches(line, pattern):
    return all([pattern[i] != "#" or line[i] == '#' for i in range(len(pattern))])

def check_for_monster(image, topLineNumber):
    PATTERN1 = "                  # "
    PATTERN2 = "#    ##    ##    ###"
    PATTERN3 = " #  #  #  #  #  #   "

    topLine = ''.join(image[topLineNumber])
    middleLine = ''.join(image[topLineNumber + 1])
    bottomLine = ''.join(image[topLineNumber + 2])

    return any([pattern_matches(topLine[offset:], PATTERN1) and \
                pattern_matches(middleLine[offset:], PATTERN2) and \
                pattern_matches(bottomLine[offset:], PATTERN3) for offset in range(len(topLine) - len(PATTERN1))])

def count_monsters_in_image(image):
    return sum([1 for topLineNumber in range(len(image) - 2) if check_for_monster(image, topLineNumber)])

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
    for _ in range(2):
        for _ in range(4):
            count = count_monsters_in_image(image)
            if count != 0: return count
            image = list(zip(*image[::-1]))
        image = image[::-1]

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