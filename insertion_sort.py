def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr

