s=input("enter the string")
print(s)
x=len(s)
q={}
a=0
while(x>0):
    if (s[a] in q.keys()):
       q[s[a]]=q[s[a]]+1
    else:
        q[s[a]]=1
    a+=1
    x-=1
print(q)

