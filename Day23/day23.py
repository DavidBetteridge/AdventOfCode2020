import time

def cups_for_part_one():
    numberOfCups = 9
    cups = [i+1 for i in range(numberOfCups+1)]
    cups[6] = 5
    cups[5] = 3
    cups[3] = 4
    cups[4] = 2
    cups[2] = 7
    cups[7] = 9
    cups[9] = 1
    cups[1] = 8
    cups[8] = 6
    currentCup = 6
    return (currentCup, cups)

def cups_for_part_two():
    numberOfCups = 1000000
    cups = [i+1 for i in range(numberOfCups+1)]
    cups[6] = 5
    cups[5] = 3
    cups[3] = 4
    cups[4] = 2
    cups[2] = 7
    cups[7] = 9
    cups[9] = 1
    cups[1] = 8
    cups[8] = 10
    currentCup = 6
    cups[-1] = currentCup
    return (currentCup, cups)

def play(numberOfMoves, cups, currentCup):
    highestCup = max(cups)

    for _ in range(numberOfMoves):
        p1 = cups[currentCup]
        p2 = cups[p1]
        p3 = cups[p2]
        
        destinationCup = currentCup - 1
        if destinationCup < 1: destinationCup = highestCup
        while destinationCup in [p1,p2,p3]:
            destinationCup -= 1
            if destinationCup < 1: destinationCup = highestCup

        cups[currentCup] = cups[p3]

        cups[p3] = cups[destinationCup]
        cups[destinationCup] = p1

        currentCup = cups[currentCup]

def time_it(func):
    def wrapper():
        tic = time.perf_counter()
        result = func()
        toc = time.perf_counter()
        print(f"Solved in {toc - tic:0.4f} seconds")   
        return result
    return wrapper

@time_it
def part_one():
    currentCup, cups = cups_for_part_one()
    play(100, cups, currentCup)
    result = ""
    i = cups[1]
    while i != 1:
        result += str(i)
        i = cups[i]
    return result

@time_it
def part_two():
    currentCup, cups = cups_for_part_two()
    play(10000000, cups, currentCup)
    return cups[1] * cups[cups[1]]

print(part_one())    #76952348
print(part_two())    #72772522064     16.6864 seconds