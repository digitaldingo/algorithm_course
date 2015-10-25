import numpy as np

from IPython import embed


def partition(arr, l, r):
    p = arr[l]  # Choose pivot
    i = l+1

    for j in range(l+1, r):
        if arr[j] < p:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

            i += 1

    t = arr[i-1]
    arr[i-1] = arr[l]
    arr[l] = t




if __name__ == "__main__":

    a = np.random.randint(0, 10, 10)

    partition(a, 0, 10)
