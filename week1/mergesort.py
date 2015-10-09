import time

import numpy as np

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


if __name__ == "__main__":

    timings = 10

    #n_list = list(range(100, 2000, 50))
    n_list = np.logspace(2, 5, 20, dtype=int)
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

    fig, ax = plt.subplots()

    ax.errorbar(n_list, meantimes, stdtimes, fmt='none', ecolor=seapal[0])
    ax.plot(n_list, meantimes, ls='', marker="o", ms=6)

    ax.set_title("Merge sort running time ({} repititions)".format(timings))
    ax.set_xlabel("Array size")
    ax.set_ylabel("Running time")

    plt.tight_layout()
    plt.show(block=False)

    embed()
