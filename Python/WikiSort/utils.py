def swap(a,b):
    return b,a

def blockSwap(arr, idx1, idx2, count):
    idx = idx1
    count = 0
    while idx1 <= idx <= idx2:
        tmp = arr[idx1 + count]
        arr[idx1 + count] = arr[idx2 + count]
        arr[idx2 + count] = tmp
        count += 1
        idx +=1
    return arr

def reverse(arr, idxRange):
    index = abs(idxRange[0] - idxRange[1])/2
    while (index >=0):
        t1, t2 = swap(arr[idxRange[0] + index], arr[idxRange[1] - index -1])
        arr[idxRange[0] + index] = t1
        arr[idxRange[1] - index -1] = t2
        index -= 1
    return arr

def rotate(arr, idxRange, count):
    arr = reverse(arr, (idxRange[0], count))
    arr = reverse(arr, (idxRange[0] + count, idxRange[1]))
    arr = reverse(arr, idxRange)
    pass


