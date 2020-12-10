lines = sorted(map(int,open('Day10/day10.txt').read().splitlines()))

oneCount=0
threeCount=1

if lines[0] == 1:
    oneCount += 1

if lines[0] == 3:
    threeCount += 1

for i in range(0, len(lines) - 1):
    if lines[i + 1] - lines[i] == 1:
        oneCount += 1
    if lines[i + 1] - lines[i] == 3:
        threeCount += 1

print(oneCount)        
print(threeCount)        

print(oneCount * threeCount)

#2170