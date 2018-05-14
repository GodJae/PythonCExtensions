import std
import stdcy
import stdcyc
import stdcyt
import stdpy
import numpy as np

import random

random.seed(100)
rands = [random.random() for _ in range(0, 5)]
cyc_rands = stdcyc.pystd(rands)
cyt_rands = stdcyt.pystd(rands)

print('std: ', std.standard_dev(rands))
print('stdcy: ', stdcy.standard_dev(rands))
print('stdcyc: ', cyc_rands.standard_dev())
print('stdcyt: ', cyt_rands.standard_dev())
print('stdpy: ', stdpy.standard_dev(rands))
print('numpy: ', np.std(rands))
