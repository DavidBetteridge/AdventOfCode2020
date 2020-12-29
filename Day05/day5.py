seatIds = list(map(lambda line: int(line.replace('B','1').replace('F','0').replace('R','1').replace('L','0'), 2), open('Day05/day5.txt').read().splitlines()))

def part_one():
    return max(seatIds)

def part_two():    
    return next((seatId for seatId in range(min(seatIds), max(seatIds)) if (not seatId in seatIds)), None)


print(part_two())