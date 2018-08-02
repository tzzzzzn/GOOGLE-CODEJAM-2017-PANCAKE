def insertionsort(mylist):
    k=len(mylist)
    for x in range(0,k):
        i=x-1
        while(mylist[x]<mylist[i] and (x>0)):
            mylist[x],mylist[i]=mylist[i],mylist[x]
            x=x-1
            i=i-1
    return mylist
l=[45,12,7,36,74,10,89]
print(insertionsort(l))
    
