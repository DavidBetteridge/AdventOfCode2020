def part_one():
    earliest, busIds = open('Day13/day13.txt').read().splitlines()
    earliest = int(earliest)    

    busIds = list([int(i) for i in busIds.split(',') if i != 'x'])
    waitTill = earliest
    while True:
        for b in busIds:
            if waitTill % b == 0:
                print(f'Bus {b} at {waitTill}')
                print( b * (waitTill - earliest) )
                break
        waitTill += 1            


def part_two():
    _, busIds = open('Day13/day13.txt').read().splitlines()
    busIds = busIds.split(',')
    firstBus = int(busIds[0])

    buses = (list([(int(b),i) for i,b in enumerate(busIds) if b != 'x']))[1:]

    t = firstBus
    while True:
        matches = [b for (b,offset) in buses if (t + offset) % b == 0]
        if len(matches) == len(buses):
            print(t)

        step = firstBus
        for s in matches: 
            step *= s

        t += step

part_two()        

