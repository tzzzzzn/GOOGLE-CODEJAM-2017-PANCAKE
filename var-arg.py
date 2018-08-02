def f1(*n):
    result=0
    print('var-arg function',len(n))
    for x in n:
        result=result+x
    print(result)
f1()
f1(10)
f1(10,20)
f1(10,20,30)
