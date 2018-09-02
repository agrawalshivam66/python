def fib_range(x):
    print("First fibonacci numbers in range 1-1000 are") 
    a=0
    b=1
    c=0
    while c<x:
        print(c,end=', ')
        c=a+b
        a=b
        b=c

def fib_first():
    print("First 25 fibonacci numbers are") 
    a=0
    b=1
    c=0
    count=0
    while count<25:
        print(c,end=', ')
        c=a+b
        a=b
        b=c
        count+=1
        
fib_range(1000)
fib_first()
