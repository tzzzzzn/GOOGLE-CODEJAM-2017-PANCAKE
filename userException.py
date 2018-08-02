class m(Exception):
    print('hello')
    
try:
    raise m
except:
    print('nothing')
print('the end')
