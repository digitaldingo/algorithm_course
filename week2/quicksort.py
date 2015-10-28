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

    return i-1


def quicksort(arr):
    if len(arr) == 1:
        return

    p = partition(arr, 0, len(arr))

    if p > 0:
        quicksort(arr[:p])

    if p < len(arr)-1:
        quicksort(arr[p+1:])

    return


if __name__ == "__main__":
    #np.random.seed(4)

    for i in range(5):
        a = np.random.randint(0, 10, 10)
        #a = np.arange(10)
        #np.random.shuffle(a)
        print(a)

        quicksort(a)
        print(a)

        print("--------------")
