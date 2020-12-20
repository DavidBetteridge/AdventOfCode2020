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

def part_one():
    tiles = read_file()

    result = 1
    for tile in tiles:
        matches = []
        matches += find_matches(tiles, tile, tile.top_border())
        matches += find_matches(tiles, tile, tile.bottom_border())
        matches += find_matches(tiles, tile, tile.left_border())
        matches += find_matches(tiles, tile, tile.right_border())                
        if len(matches) == 2:
            result *= tile.TileId
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

tiles = read_file()

grid = []
gridSize = int(math.sqrt(len(tiles)))

topLeft = find_top_left_corner(tiles)
tiles.pop(topLeft.TileId, None)

row = [topLeft]
grid.append(row)
complete_row(row, gridSize, tiles)

for _ in range(gridSize - 1):
    row = new_row(tiles, grid)
    complete_row(row, gridSize, tiles)
