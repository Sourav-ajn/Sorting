def mergeSort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return mergeSortedArrays(mergeSort(left), mergeSort(right))

def mergeSortedArrays(left, right):
    res = [None] * (len(left) + len(right))

    k = i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1
    return res
