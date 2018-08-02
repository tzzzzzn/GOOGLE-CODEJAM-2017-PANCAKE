l=[45,78,96,12,0,7]
def bubblesort(array):
    k=len(array)
    for i in range(0,k):
        for j in range(0,k-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    return array
print(bubblesort(l))
