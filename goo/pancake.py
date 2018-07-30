m=open("large.in")
o=open("correct.in","a")
print(m.read())
m.seek(0)
q=int(m.readline())
f=0
p=[]
for f in range(1,q+1):
    o.write('Case #'+str(f)+': ')
    j=m.readline()
    k,n=j.split(' ')
    k=k.strip()
    n=n.strip()
    s=[]
    n=int(n)
    for x in k:
        s.append(x)
    counter=0
    def call(x,y):
        global s
        if(y>=len(s)):
            return
        for i in range(x,y+1):
            if s[i]=='-':
                s[i]='+'
            else:
                s[i]='-'
        return
    for i in range(len(s)):
        if len(s)==s.count('+'):
            break
        if(s[i]=='+'):
            continue
        else:
            call(i,i+n-1)
            counter+=1
    if len(s)==s.count('+'):
        o.write(str(counter))
    else:
        o.write('IMPOSSIBLE')
    o.write("\n")
o.close()
m.close()
