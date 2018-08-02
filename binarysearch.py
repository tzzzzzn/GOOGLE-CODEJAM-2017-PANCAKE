def binary(myitem,mylist):
    start=0
    end=len(mylist)-1
    middle=(start+end)//2
    while(start<end and mylist[middle]!=myitem):
        if(mylist[middle]==myitem):
            break
        elif(mylist[middle]<myitem):
            start=middle+1
            #start=middle
            print(start)
        else:
            end=middle-1
            print(end)
        middle=(start+end)//2
    if(mylist[middle]==myitem):
        return middle       
l=[1,5,8,12,20,35,40,51,69,80]
print(l)
n=eval(input("enter the number u want to search"))
x=binary(n,l)
if(x==-1):
    print("element not present")
else:
    print("element found at index",x)
