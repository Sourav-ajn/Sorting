def heapSort(array):
    buildMaxHeap(array)
    for end in reversed(range(1,len(array))):
        swap(0,end, array)
        siftDown(0,end-1,array)
    return array

def buildMaxHeap(array):
    currentIdx=len(array)//2
    for i in reversed(range(0,currentIdx)):
        siftDown(i,len(array)-1,array)
    
def siftDown(curr, end, array):
    childOne = curr * 2 + 1
    while childOne <= end:
        childTwo = curr * 2 + 2 if curr * 2 + 2 <= end else -1
        if childTwo > -1 and array[childTwo] > array[childOne]:
            swapIndex = childTwo
        else:
            swapIndex = childOne
        if array[swapIndex] > array[curr]:
            swap(curr, swapIndex, array)
            curr = swapIndex
            childOne = curr * 2 + 1
        else:
            return
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
