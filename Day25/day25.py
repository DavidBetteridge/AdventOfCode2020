
def find_loop_size(targetKey):
    subjectNumber = 7
    value = 1
    loopSize = 0
    while value != targetKey:
        loopSize += 1
        value = value * subjectNumber
        value = value % 20201227
    return loopSize



cardPublicKey = 9789649
doorPublicKey = 3647239

print(find_loop_size(cardPublicKey))
print(find_loop_size(doorPublicKey))

subjectNumber = doorPublicKey
value = 1
for _ in range(find_loop_size(cardPublicKey)):
    value = value * subjectNumber
    value = value % 20201227
print(value)    