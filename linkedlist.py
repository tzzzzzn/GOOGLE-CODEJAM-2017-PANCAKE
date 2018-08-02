class element:
    def __init__(self,value):
        self.value=value
        self.nextadd=None
class linkedlist(element):
    def __init__(self,head=None):
        self.head=head
    def add(self,element):
        cur=self.head
        if self.head!=None:
            while cur.nextadd:
                cur=cur.nextadd
            cur.nextadd=element
        else:
            self.head=element
    def display(self):
        c=self.head
        while(c.nextadd != None):
            print(c.value,end=' ')
            c=c.nextadd
        print(c.value)
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        i=0
        if position==0:
            return None
        c=self.head
        while(i!=position and c.nextadd!=None):
            c=c.nextadd
            i+=1
        return c.value
x='x'
while x!='y':
    y=input('1.create\n2.add\n3.display\n4.get_position(self, position)')
    if y=='1':
        k=linkedlist()
    elif y=='2':
        z=element(eval(input("enter the value")))
        k.add(z)
    elif y=='3':
        k.display()
    else:
        print(k.get_position(int(input('enter the position'))))
    x=input("x to continue\ny to stop")
        
