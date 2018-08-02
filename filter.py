def eve(x):
    if(x%2==0):
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9]
l1=list(filter(eve,l))
print(l1)
