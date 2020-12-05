def calculate_seatId(line):
    rowBinary = line[:7].replace('B','1').replace('F','0')
    seatBinary = line[7:].replace('R','1').replace('L','0')
    row = int(rowBinary, 2)
    seat = int(seatBinary, 2)
    return (row * 8) + seat

boardingPasses = open('Day5/day5.txt').read().splitlines()
seatIds = list(map(calculate_seatId, boardingPasses))
highestSeatId = max(seatIds)
print(highestSeatId)

for row in range(int('0000001',2), int('1111110',2)):
    for column in range(0,7):
        seatId = (row * 8) + column
        if not seatId in seatIds:
            if (seatId - 1 in seatIds) and (seatId + 1 in seatIds):
                print(seatId)
