import std
import stdcy
import stdpy
import numpy as np

import random

random.seed(100)
rands = [random.random() for _ in range(0, 5)]

print('std: ', std.standard_dev(rands))
print('stdcy: ', stdcy.standard_dev(rands))
print('stdpy: ', stdpy.standard_dev(rands))
print('numpy: ', np.std(rands))
