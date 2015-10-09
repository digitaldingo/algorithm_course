import time

import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import seaborn as sns
seapal = sns.color_palette()

from IPython import embed

def mergesort(lst):

    if len(lst) == 1:
        return lst

    idx = len(lst)//2

    sub1 = mergesort(lst[:idx])
    sub2 = mergesort(lst[idx:])

    i = j = 0

    output = [None]*len(lst)
    for k in range(len(lst)):

        if i == len(sub1):
            output[k:] = sub2[j:]
            break

        if j == len(sub2):
            output[k:] = sub1[i:]
            break

        if sub1[i] < sub2[j]:
            output[k] = sub1[i]
            i += 1
        else:
            output[k] = sub2[j]
            j += 1

    return output

def complexity(n, p):
    return p*n*(np.log2(n) + 1)


if __name__ == "__main__":

    timings = 20        # repetitions
    max_npower = 20     # max size of array: 2**max_npower

    n_list = np.logspace(2, max_npower, 20, dtype=int, base=2)
    meantimes = []
    stdtimes = []

    loop_time = time.time()
    for n in n_list:

        lst = np.random.randint(0,n,n)
        times = []

        for t in range(timings):
            start = time.time()
            sorted_list = mergesort(lst)
            times.append(time.time()-start)

        meantimes.append(np.mean(times))
        stdtimes.append(np.std(times))

    print("Looping took {:g} s".format(time.time()-loop_time))

    # Fit theoretical complexity:
    p = curve_fit(complexity, n_list, meantimes, sigma=stdtimes)[0][0]
    x = np.linspace(0, 2**max_npower, 100)
    y = complexity(x, p)

    fig, ax = plt.subplots()

    # Plot measurements:
    ax.errorbar(n_list, meantimes, stdtimes, fmt='none', ecolor=seapal[0])
    ax.plot(n_list, meantimes, ls='', marker="o", ms=6)

    # Plot complexity:
    ax.plot(x, y, alpha=.7)

    ax.set_title("Merge sort running time ({} repetitions)".format(timings))
    ax.set_xlabel("Array size")
    ax.set_ylabel("Running time")
    ax.set_xscale('log', basex=2)

    plt.tight_layout()
    plt.show(block=False)

    embed()
