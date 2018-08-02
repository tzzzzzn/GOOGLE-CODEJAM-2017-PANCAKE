#import turtle
from turtle import *
from random import*
'''refer='abcdefghijklmnopqrstuvwxyz'
def encrypt(string,k):
    l=[]
    for x in string:
        y=refer.find(x)
        if y>-1:
            if y+k<=26:
                l.append(refer[y+k])
            else:
                l.append(refer[(y+k)-26])
        else:
            l.append(x)
    print(''.join(l))
    return ''.join(l)
def decrypt(string,k):
    l=[]
    for x in string:
        y=refer.find(x)
        if y>-1:
            if y-k<=26:
                l.append(refer[y-k])
            else:
                l.append(refer[26-(k-y)])
        else:
            l.append(x)
    print(''.join(l))\'''
def team_divide(my_list):
    p2=[]
    k=len(my_list)//2
    for x in range(0,k):
        player=choice(my_list)
        p2.append(player)
        my_list.remove(player)
        print('player 1:',my_list,'player 2:',p2)
    return my_list,p2
#decrypt(encrypt(input('enter the message'),int(input('enter the key'))),int(input('enter the key')))
team_divide(eval(input('enter the list of names')))'''
s=Screen()
s.setup(400,400)
s.bgcolor('red')
