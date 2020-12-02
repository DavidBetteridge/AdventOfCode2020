import matplotlib.pyplot as plt 
import numpy as np 

numbers = {} 
for line in open('C:/personal/AdventOfCode2020/Day1/day1.txt').read().splitlines():
    numbers[int(line)] = int(line)

def fun(x, y):
    return np.subtract(2020, np.add(x,y))

def part1():
    for number in numbers:
        otherNumber = 2020 - number
        if (otherNumber in numbers):
            print(f'{number} {otherNumber} {number * otherNumber}')

    # N = sorted(numbers)
    # [X, Y] = np.meshgrid(np.array(N), np.array(N))
    # zs = np.array(fun(np.ravel(X), np.ravel(Y)))
    # Z = zs.reshape(X.shape)

    # fig = plt.figure()
    # axes = fig.gca(projection="3d")
    # axes.plot_surface(X,Y,Z,cmap="rainbow")
    # plt.contour(X,Y,Z,cmap="rainbow")
    # plt.show()    

def part2():
    sortedNumbers = sorted(numbers)
    for number1 in sortedNumbers:
        index = 0
        while (sortedNumbers[index] + number1 < 2020):
            number2 = sortedNumbers[index]
            index = index + 1
            number3 = 2020 - number2 - number1
            if (number3 in numbers):
                print(f'{number1} {number2} {number3} {number1 * number2 * number3}')            

part1()

