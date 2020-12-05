def calculate_seatId(line):
    rowBinary = line[:7].replace('B','1').replace('F','0')
    seatBinary = line[7:].replace('R','1').replace('L','0')
    row = int(rowBinary, 2)
    seat = int(seatBinary, 2)
    return (row * 8) + seat

lines = open('Day5/day5.txt').read().splitlines()
highestSeatId = max(map(calculate_seatId,lines))
print(highestSeatId)