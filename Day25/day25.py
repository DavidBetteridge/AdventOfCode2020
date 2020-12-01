import time
from numba import njit          #pip install numpy==1.19.3

def time_it(what):
    def decorator(func):
        def wrapper():
            tic = time.perf_counter()
            result = func()
            toc = time.perf_counter()
            print(f"Solved {what} in {toc - tic:0.4f} seconds")   
            return result
        return wrapper
    return decorator   

@njit
def find_loop_size(targetKey):
    subjectNumber = 7
    value = 1
    loopSize = 0
    while value != targetKey:
        loopSize += 1
        value = value * subjectNumber
        value = value % 20201227

    return loopSize

@time_it("Part One")
def part_one():
    cardPublicKey = 9789649
    doorPublicKey = 3647239

    publicCardKeyLoopSize = find_loop_size(cardPublicKey)
    value = pow(doorPublicKey, publicCardKeyLoopSize, 20201227)

    return value

print(part_one())    #8740494     Solved Part One in 0.3779 seconds