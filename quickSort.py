def quickSort(array,start, end):
    if start < end:
        pIndex= partition(array,start,end)
        quickSort(array,start,pIndex-1)
        quickSort(array,pIndex+1,end)

def partition(array, start, end):
    pivot=array[end]
    pIndex=start
    for i in range(start,end):
        if array[i]<=pivot:
            swap(i,pIndex,array)
            pIndex+=1
    swap(pIndex,end,array)
    return pIndex        

def swap(i,j,array):
    array[i],array[j]=array[j],array[i]