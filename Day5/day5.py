seatIds = list(map(lambda line: int(line.replace('B','1').replace('F','0').replace('R','1').replace('L','0'), 2), open('Day5/day5.txt').read().splitlines()))
print(max(seatIds))
print(next((seatId for seatId in range(0, 1024) if (not seatId in seatIds) and (seatId - 1 in seatIds) and (seatId + 1 in seatIds)), None))