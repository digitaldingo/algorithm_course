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

def argmedian(arr, idx):
    p1, p2, p3 = arr[idx]

    if (p1 - p2) * (p3 - p1) >= 0:
        return idx[0]
    elif (p2 - p1) * (p3 - p2) >= 0:
        return idx[1]
    else:
        return idx[2]

def quicksort(arr, pivot="start", c=None):
    if len(arr) == 1:
        return c

    if c is None:
        c = len(arr)-1

    if pivot == "start":
        pass
    elif pivot == "end":
        p0 = arr[0]
        arr[0] = arr[-1]
        arr[-1] = p0
    elif pivot == "median":
        a0 = argmedian(arr, [0,(len(arr)-1)//2,-1])
        p0 = arr[0]
        arr[0] = arr[a0]
        arr[a0] = p0

    p = partition(arr, 0, len(arr))

    if p > 0:
        c += p-1
        c = quicksort(arr[:p], pivot, c)

    if p < len(arr)-1:
        c += len(arr[p+1:]) - 1
        c = quicksort(arr[p+1:], pivot, c)

    return c


if __name__ == "__main__":
    #np.random.seed(4)

    for i in range(5):
        a = np.random.randint(0, 10, 10)
        #a = np.arange(10)
        #np.random.shuffle(a)
        print(a)

        c = quicksort(a, pivot="end")
        print(a)
        print(c)

        print("--------------")


    for p in ['start', 'end', 'median']:
        a = np.loadtxt("../../data/week2/QuickSort.txt")
        print(p)
        c = quicksort(a, pivot=p)
        print("  ", c)
