def is_prime(x):
    for i in range(2,int((x**(1/2))+1)):
        if x%i==0:
            return 1
    return 0

def primes_lessthan(n):
    a=list()
    for i in range(2,n):
        if is_prime(i)==0:
            a.append(i)
    return a

c=eval(input("Enter the number "))
b= primes_lessthan(c)
print(b)
