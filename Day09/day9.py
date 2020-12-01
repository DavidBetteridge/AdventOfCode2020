WINDOW_SIZE = 25

def check_number(window, number_to_check):
    for n1 in window:
        n2 = number_to_check - n1
        if n2 in window:
            return True
    return False

numbers = list(map(int, open('Day09/day9.txt').read().splitlines()))

def part_one():
    for i in range(WINDOW_SIZE, len(numbers)):
        window = set(numbers[i-WINDOW_SIZE:i])
        number_to_check = numbers[i]
        if not check_number(window, number_to_check):
            return number_to_check

def find_range(targetNumber):
    for i in range(0, len(numbers)):
        running_total = 0
        offset = 0
        while running_total < targetNumber:
            running_total += numbers[i + offset]
            offset += 1

        if running_total == targetNumber:
            return numbers[i:i+offset]

def part_two():
    targetNumber = part_one()
    window = find_range(targetNumber)
    return min(window) + max(window)