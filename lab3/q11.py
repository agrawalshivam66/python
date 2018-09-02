def a(n):
    print("a")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(j,end=' ')
        print('')

def b(n):
    print("b")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(i,end=' ')
        print('')
        
def c(n):
    print("c")
    for i in range(1,n+1):
        for j in range (1,n+1-i):
            print(end=' ')
        for k in range(1,i+1):
            print("*",end='')
        print('')
        
def d(n):
    print("d")
    for i in range(n,0,-1):
        for j in range (1,n+1-i):
            print(end=' ')
        for k in range(1,i+1):
            print("*",end='')
        print('')

def e(n):
    print("e")
    count=1
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(count,end=' ')
            count+=1
        print('')

def f(n):
    print("f")
    for i in range(1,n+1):
        for j in range (i,0,-1):
            print(j,end=' ')
        print('')

def g(n):
    print("g")
    c=1
    for i in range(1,n+1):
        for j in range (1,i+1):
           print(c,end=' ')
           if c==0:
               c=1
           else:
               c=0
        print('')

def h(n):
    print("h")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(j,end=' ')
        print('')

def m(n):
    print("m")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print("*",end=' ')
        print('')
    for i in range(n-1,0,-1):
        for k in range (i+1,1,-1):
            print("*",end=' ')
        print('')

a(5)
b(5)
e(5)
c(5)
d(5)
f(5)
g(5)
m(5)
