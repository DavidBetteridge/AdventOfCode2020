numbers = set()
for line in open('Day01/day1.txt').read().splitlines():
    numbers.add(int(line))

def part_one():
    for number in numbers:
        otherNumber = 2020 - number
        if (otherNumber in numbers):
            return number * otherNumber

def part_two():
    sortedNumbers = sorted(numbers)
    for number1 in numbers:
        index = 0
        while (sortedNumbers[index] + number1 < 2020):
            number2 = sortedNumbers[index]
            index = index + 1
            number3 = 2020 - number2 - number1
            if (number3 in numbers):
                return number1 * number2 * number3