def shellSort(array):
    size = len(array)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            j = i
            while j>=gap and array[j-gap]>array[j]:
                array[j], array[j-gap] = array[j-gap], array[j]
                j -= gap
        gap = gap // 2

