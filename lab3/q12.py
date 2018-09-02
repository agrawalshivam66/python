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
    x=float(input(" Enter the value for x : "))
    x=(x*math.pi)/180  #convert degree into radian
    term=x
    sum=x
    i=2
    while abs(term) >= 0.000001: # until the absolute value of the nth term is less than the desired acceptable error
        term *= (-x*x)/((2*i-2)*(2*i-1))
        sum=sum+term
        i+=1
    print("The value of Sin(x) = ",sum)

sixth(n)
