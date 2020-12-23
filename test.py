import time

tic = time.perf_counter()
for _ in range(10000000):
    pass
toc = time.perf_counter()
print(f"Played in in {toc - tic:0.4f} seconds")