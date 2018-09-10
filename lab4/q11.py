def divisors(n):
    sum=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    return sum

def amicable():
    for a in range(1,10001):
        b=divisors(a)
        d_b=divisors(b)
        if d_b==a and a!=b:
            print(a,end=' ')

def amicable_pair(a,b):
        x=divisors(a)
        y=divisors(b)
        if x==b and y==a and a!=b:
            return 1
        else:
            return 0
        
print(amicable_pair(220,284))
amicable()

