def countingSort(array):
    max = maxelemInArray(array)
    count=[0]*max
    output=[0]*max
    for i in array:
        count[i]+=1
    for i in reversed(range(0,len(array))):
       index=count[array[i]]-1
       output[index]=array[i]
       count[array[i]]-=1

    return output

def maxelemInArray(array):
    max=float('inf')
    for i in array:
        if i>max:
            max=i
    return max
