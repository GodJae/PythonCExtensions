import stdcyc
import stdcyt
import time
import timeit

import random

def elapsed(t):
    return str(round(t, 3)) + " seconds."

random.seed(100)

item_size = 200000000

print('{:,} elements'.format(item_size))
print('--')

m1_1 = time.time()
rands = [random.random() for _ in range(0, item_size)]
m1_2 = time.time()
print('generate rands: ', elapsed(m1_2 - m1_1))

# m3_1 = time.time()
# cyc_rands = stdcyc.pystd(rands)
# m3_2 = time.time()
m2_1 = time.time()
cyt_rands = stdcyt.pystd(rands)
m2_2 = time.time()

# print('type conversion(stdcyc): ', elapsed(m3_2 - m3_1))
print('type conversion(stdcyt): ', elapsed(m2_2 - m2_1))

print()

# print('stdcyc elapsed: ', elapsed(timeit.timeit(lambda: cyc_rands.standard_dev(), number=1)))
print('stdcyt elapsed: ', elapsed(timeit.timeit(lambda: cyt_rands.standard_dev(), number=1)))
