def display_cups(currentCup, cups):
    s = "(" + str(currentCup) + ")"
    c = cups[currentCup]
    while c != currentCup:
        s += "," + str(c)
        c = cups[c]
    print('cups:', s)

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


# cups[3] = 8
# cups[8] = 9
# cups[9] = 1
# cups[1] = 2
# cups[2] = 5
# cups[5] = 4
# cups[4] = 6
# cups[6] = 7
# cups[7] = 10
# currentCup = 3

cups[-1] = currentCup

highestLabel = max(cups)
moveNumber = 0

for _ in range(10000000):
    #moveNumber += 1
    #print(f'-- move{moveNumber} --')

    #display_cups(currentCup, cups)

    pickup = [cups[currentCup], cups[cups[currentCup]], cups[cups[cups[currentCup]]]]

    #print('pick up:', ' '.join([str(c) for c in pickup]))

    destinationCup = currentCup - 1
    if destinationCup < 1: destinationCup = highestLabel
    while destinationCup in pickup:
        destinationCup -= 1
        if destinationCup < 1: destinationCup = highestLabel

    # print('destination:', destinationCup)
    # print('')

    cups[currentCup] = cups[cups[cups[cups[currentCup]]]] #Removed

    next = cups[destinationCup]
    cups[destinationCup] = pickup[0]
    cups[pickup[-1]] = next

    currentCup = cups[currentCup]

def part_one():
    result = ""
    i = cups[1]
    while i != 1:
        result += str(i)
        i = cups[i]
    print(result)    

print(cups[1])
print(cups[cups[1]])
print(cups[1] * cups[cups[1]])


#cups = [6,5,3,4,2,7,9,1,8]
#76952348