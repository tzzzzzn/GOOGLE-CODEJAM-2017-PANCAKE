class MyClass:
    "This is my second class"
    a = 10#class variable
    __private='value'#private data
    def __init__(self):#constructor
        print('Hello')
        print(self.__private)#accessing private data
print(MyClass.__doc__)
z=MyClass()#constructor will be called automatically
print(z.a)
'''print(z.__private)'''#this will raise an error as it is private
print(z._MyClass__private)#so no data is private in python

