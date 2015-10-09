import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

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

    n = 42

    lst = list(range(n))
    np.random.shuffle(lst)
    lst = np.random.randint(0,n,n)

    sorted_list = mergesort(lst)

    embed()
