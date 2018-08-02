#                                                                          password                                                                                                                                                                                                                                                                                                                                                                                
from random import *
p='abcdefghijklmnopqrstuvwxyz'
def start():
    if password():
        
        
   
def password():
    x=input('Enter the User name')
    if x=='tzzzzzn':
        k=open('password.txt','w+')
        k.seek(0)
        k.write(p[randint(0,26)]+p[randint(0,26)]+p[randint(0,26)]+p[randint(0,26)]+p[randint(0,26)]+p[randint(0,26)])
        k.seek(0)
        h=k.read(6)
        k.close()
        if(input('enter the password')==h):
            print('you are logged in')
            return 1
        else:
            print('you entered wrong password')
            return 0
    else:
        return 0
start()
