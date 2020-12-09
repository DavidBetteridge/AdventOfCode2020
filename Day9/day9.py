WINDOW_SIZE = 25

def check_number(window, number_to_check):
    for n1 in window:
        n2 = number_to_check - n1
        if n1 != n2 and n2 in window:
            return True
    return False

numbers = list(map(int, open('Day9/day9.txt').read().splitlines()))

for i in range(WINDOW_SIZE, len(numbers)):
    window = numbers[i-WINDOW_SIZE:i]
    number_to_check = numbers[i]
    if not check_number(window, number_to_check):
        print(number_to_check)

    