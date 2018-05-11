import numpy as np
import random
import timeit
import math
import pandas as pd
from matplotlib import pyplot as plt
import std


def mean(lst):
    return sum(lst) / len(lst)


def standard_deviation(lst):
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))


if __name__ == '__main__':
    start = 100; end = 1000; step = 10; include_pure_py = True
    # start = 10000; end = 30000; step = 1000; include_pure_py = False
    lens = range(start, end, step)
    py_time = []
    np_time = []
    c_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        numpy_rands = np.array(rands)
        if include_pure_py:
            py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=1000))
        np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=1000))
        c_time = np.append(c_time, timeit.timeit(lambda: std.standard_dev(rands), number=1000))
    if include_pure_py:
        data = np.array([np.transpose(py_time), np.transpose(np_time), np.transpose(c_time)])
    else:
        data = np.array([np.transpose(np_time), np.transpose(c_time)])

    if include_pure_py:
        df = pd.DataFrame(data.transpose(), index=lens, columns=['Python', 'Numpy', 'C++'])
    else:
        df = pd.DataFrame(data.transpose(), index=lens, columns=['Numpy', 'C++'])
    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.ylabel('Time (Seconds)')
    plt.xlabel('Number of Elements')
    plt.title('1k Runs of Standard Deviation')
    plt.show()
