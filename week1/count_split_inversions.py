import time

import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import seaborn as sns
seapal = sns.color_palette()

from IPython import embed

def merge_and_count_split_inversions(lst, c=None):

    if len(lst) == 1:
        return lst, c

    if c is None:
        c = 0

    idx = len(lst)//2

    sub1, c = merge_and_count_split_inversions(lst[:idx], c)
    sub2, c = merge_and_count_split_inversions(lst[idx:], c)

    i = j = 0

    output = [None]*len(lst)
    for k in range(len(lst)):

        if i == len(sub1):
            output[k:] = sub2[j:]
            break

        if j == len(sub2):
            output[k:] = sub1[i:]
            break

        if sub1[i] <= sub2[j]:
            output[k] = sub1[i]
            i += 1
        else:
            output[k] = sub2[j]
            j += 1
            c += len(sub1) - i

    return output, c

def complexity(n, p):
    return p*n*(np.log2(n) + 1)


if __name__ == "__main__":


    timings = 50        # repetitions
    max_npower = 15     # max size of array: 2**max_npower

    n_list = np.logspace(2, max_npower, 20, dtype=int, base=2)
    meantimes = []
    stdtimes = []

    loop_time = time.time()
    for n in n_list:

        times = []

        for t in range(timings):
            lst = np.random.randint(0,n,n)
            start = time.time()
            sorted_list, c = merge_and_count_split_inversions(lst)
            times.append(time.time()-start)

        meantimes.append(np.mean(times))
        stdtimes.append(np.std(times))

    print("Looping took {:g} s".format(time.time()-loop_time))

    # Fit theoretical complexity:
    p = curve_fit(complexity, n_list, meantimes, sigma=stdtimes)[0][0]
    x = np.linspace(0, 2**max_npower, 100)
    y = complexity(x, p)

    fig, ax = plt.subplots(figsize=(7,4))

    # Plot measurements:
    ax.errorbar(n_list, meantimes, stdtimes, fmt='none', ecolor=seapal[0])
    ax.plot(n_list, meantimes, ls='', marker="o", ms=6,
                label='Measurements')

    # Plot complexity:
    ax.plot(x, y, alpha=.7, label='Theoretical complexity')

    ax.set_title(("Merge sort and counting split inversion running time ({} "
                  "repetitions)").format(timings))
    ax.set_xlabel("Array size")
    ax.set_ylabel("Running time")
    ax.set_xscale('log', basex=2)

    plt.legend(loc='upper left')

    plt.tight_layout()
    #plt.show(block=False)
    plt.savefig('../../figures/week1/inversioncount.svg')

    #embed()
