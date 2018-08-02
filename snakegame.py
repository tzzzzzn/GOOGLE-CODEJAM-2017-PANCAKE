from random import *
from time import *
def a():
    p=[]
    for i in range(50):
        p.append("  ")
    return p
shape=[]
for i in range(50):
    b=a()                               
    shape.insert(60,b)
x=randint(1,50)
shape[x][x]="O"
q=[x]
def main():
    global shape
    for i in range(1,50):
        shape[1][i]="--"
        shape[49][i]="--"
    food()
    display()
    return
def food():
    global shape
    x=randint(1,49)
    while(x in q):
        x=randint(1,49)
    shape[x][x]="."
    
def display():
    global shape
    for i in shape:
        for x in i:
            print(x,end=" ")
        print()
def move():
    x=int(input())
    if(x==4):
        
if  __name__=="__main__":
    main()
