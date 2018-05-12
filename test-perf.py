import numpy as np
import random
import timeit
import math
import pandas as pd
from matplotlib import pyplot as plt
import std
import stdcy


def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))


if __name__ == '__main__':
    start = 100; end = 1000; step = 10; include_pure_py = True
    # start = 100; end = 50000; step = 2000; include_pure_py = False
    lens = range(start, end, step)
    py_time = []
    np_time = []
    c_time = []
    cy_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        numpy_rands = np.array(rands)  # If you don't do this, It will convert every time
                                       # and there will be a some performance issues.

        if include_pure_py:
            py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=1000))
            np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=1000))
            c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=1000))
            cy_time = np.append(cy_time, timeit.timeit(lambda: stdcy.standard_dev(rands), number=1000))

            data = np.array([np.transpose(py_time), np.transpose(np_time), np.transpose(c_time), np.transpose(cy_time)])
        else:
            np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=1000))
            c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=1000))
            cy_time = np.append(cy_time, timeit.timeit(lambda: stdcy.standard_dev(rands), number=1000))

            data = np.array([np.transpose(np_time), np.transpose(c_time), np.transpose(cy_time)])

    if include_pure_py:
        df = pd.DataFrame(data.transpose(), index=lens, columns=['Python', 'Numpy', 'C++', 'Cython'])
    else:
        df = pd.DataFrame(data.transpose(), index=lens, columns=['Numpy', 'C++', 'Cython'])

    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.ylabel('Time (Seconds)')
    plt.xlabel('Number of Elements')
    plt.title('1k Runs of Standard Deviation')
    plt.show()
