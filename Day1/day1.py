numbers = {} 
for line in open('C:/personal/AdventOfCode2020/Day1/day1.txt').read().splitlines():
    numbers[int(line)] = int(line)

def part1():
    for number in numbers:
        otherNumber = 2020 - number
        if (otherNumber in numbers):
            print(f'{number} {otherNumber} {number * otherNumber}')


part1()