class Tile:
    def __init__(self, tileId):
        self.TileId = tileId
        self.Lines = []

    def __repr__(self):
        return f"TileId : {self.TileId}"

    def top_border(self):
        return self.Lines[0]

    def bottom_border(self):
        return self.Lines[-1]

    def left_border(self):
        result = ""
        for l in self.Lines:
            result += l[0]
        return result

    def right_border(self):
        result = ""
        for l in self.Lines:
            result += l[-1]
        return result

    def all_borders(self):
        return set([ self.top_border(), self.top_border()[::-1], 
                 self.bottom_border(), self.bottom_border()[::-1],
                 self.left_border(), self.left_border()[::-1],
                 self.right_border(), self.right_border()[::-1] 
               ])


def read_file():
    lines =  open('Day20/day20.txt').read().splitlines()

    tiles = []
    for i in range(0, len(lines), 12):

        tileId = int(lines[i].replace("Tile ", "").replace(":", ""))
        tile = Tile(tileId)

        for r in range(1, 11):
            tile.Lines.append(lines[i + r])

        tiles.append(tile)
    return tiles        

def has_match(tiles, tile, edge):
    result = []
    for otherTile in tiles:
        if otherTile.TileId != tile.TileId:
            if edge in otherTile.all_borders():
                result.append(otherTile.TileId)
    return result

def part_one():
    tiles = read_file()

    result = 1
    for tile in tiles:
        matches = []
        matches += has_match(tiles, tile, tile.top_border())
        matches += has_match(tiles, tile, tile.bottom_border())
        matches += has_match(tiles, tile, tile.left_border())
        matches += has_match(tiles, tile, tile.right_border())                
        if len(matches) == 2:
            result *= tile.TileId
    return result

print(part_one())        

