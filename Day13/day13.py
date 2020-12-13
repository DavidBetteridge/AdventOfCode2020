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