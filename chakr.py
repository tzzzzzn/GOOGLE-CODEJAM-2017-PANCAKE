x=int(input("enter the size of matrix"))
a=[]
y=x
while(y>0):
    q=[]
    for z in range(x):
        q.append(' ')
    a.insert(x+1,q)
    y-=1
z=1
l=x+1
ux=0
vy=x-1
xx=x-1
wy=0
while(z<=x*x):
    l=l-1
    for n in range(ux,l):
        a[ux][n]=z
        z+=1
    ux+=1
    for n in range(ux,l):
        a[n][vy]=z
        z+=1
    vy-=1
    for n in range(vy,wy-1,-1):
        a[xx][n]=z
        z+=1
    xx-=1
    for n in range(xx,ux-1,-1):
        a[n][wy]=z
        z+=1
    wy+=1
for p in a:
    for x in p:
        print(x,end='             ')
    print()
    print()
  
        
    
    
