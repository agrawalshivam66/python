def first(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i*i)
    print(sum)

def second(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=j
    print(sum)

def third(n):
    sum=0
    sum1=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum1*=j
        sum+=sum1
        sum1=1
    print(sum)

def forth(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i**i)
    print(sum)

def fifth(n):
    sum=0
    sum1=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum1*=j
        sum+=(sum1//i)
        sum1=1
    print(sum)

def sixth(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=(i**i)
    print(sum)
    
fifth(5)
