def fun(n):
    b=[]
    for x in range(n):
        b.append(" ")
    return b
def chakravuyha(l,b):
    z=[]
    for x in range(l):
        z.insert(100,fun(b))
    x=1
    i=0
    a=l
    c=b
    q=0
    w=0
    p=0
    u=l-1
    while(x<(l*b+1)):
        y=0
        while(y<c):
            c-=i
            if(q%2==0):
                for j in range(0,c):
                    z[p][c-1]=x
                    print(x,end=" ")
                    x+=1
                    y+=1
                print("\n")
                p+=1
            else:
                for j in range(0,c):
                    print((x+c-j-1),end=" ")
                    z[b-p][c-j-1]=x+c-j-1
                    y+=1
                x+=c
                print()
        if(x>=l*b):
            break
        y=0
        i=1
        while(y<a):
            a-=i
            if(q%2==0):
                for j in range(0,a):
                    z[j][u]=x
                    print(x,end=" ")
                    x+=1
                    y+=1
                print("\n")
                u-=1
            else:
                for j in range(0,a):
                    print((x+a-j-1),end=" ")
                    y+=1
                x+=a
                print()
        q+=1
        #print(z)
            
        
chakravuyha(4,4)
        
