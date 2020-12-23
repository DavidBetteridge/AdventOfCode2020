def format_cup(currentCup, cup):
    if currentCup == cup:
        return f'({cup})'
    else:
        return str(cup)

cups = [6,5,3,4,2,7,9,1,8]
#cups = [3,8,9,1,2,5,4,6,7]
currentCupIndex = 0
lowestLabel = min(cups)
highestLabel = max(cups)
moveNumber = 0

for _ in range(100):
    moveNumber += 1
    print(f'-- move{moveNumber} --')

    currentCup = cups[currentCupIndex]
    print('cups:', ' '.join([format_cup(currentCup, c) for c in cups]))

    pickup = (cups + cups)[currentCupIndex+1:currentCupIndex+4]
    print('pick up:', ' '.join([str(c) for c in pickup]))

    destinationCup = currentCup - 1
    if destinationCup < lowestLabel: destinationCup = highestLabel
    while destinationCup in pickup:
        destinationCup -= 1
        if destinationCup < lowestLabel: destinationCup = highestLabel

    print('destination:', destinationCup)
    print('')

    for p in pickup:
        cups.remove(p)

    destinationCupIndex = cups.index(destinationCup)

    cups = cups[:destinationCupIndex+1] + pickup + cups[destinationCupIndex+1:]

    currentCupIndex = (cups.index(currentCup) + 1) % len(cups)

result = ""
i = cups.index(1)
for _ in range(len(cups)-1):
    i = (i + 1) % len(cups)
    result += str(cups[i])
print(result)    
