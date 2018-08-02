'''
10,3

1+4+5
1+2+7
1+3+6
2+3+5
'''
from math import sqrt
n,y=input().split(',')
n=int(n)
y=int(y)
a=[]
s=1
x=1
q=[]
for z in range(y):
    q.append(' ')
while(s<n):
    s=x*x
    if(s<n):
        a.append(x*x)
    x+=1
print(a)
print(q)
d={}
for i in range(1,n):
    q[0]=i
    for x in range(i,n):
        q[1]=x
        for y in range(x,n):
            q[2]=y
            if(sum(q)==n):
                d[str(q[0])+'*'+str(q[1])+'*'+str(q[2])]='10'
print(d.keys())    

def retur(index,size):
    









    

