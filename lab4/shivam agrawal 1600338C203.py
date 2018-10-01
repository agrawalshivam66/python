# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 09:41:32 2018

@author: Shivam-PC
"""

#q1
def is_multiple(n, m):
    if n>m:
        if n%m==0:
            return True
        else:
            return False
    else:
        if m%n==0:
            return True
        else:
            return False
        
is_multiple(11,120)
is_multiple(15,120)

#q2
def is_even(n):
    return (n&1)
def second():
    input1 = int(input("Enter a number"))
    if(is_even(input1)):
        return False
    else:
        return True
print(second())

#q3 
def third():
    input1 = eval(input("Enter a number:")) 
    while (input1<0) or (type(input1)!=int):
        input1 = eval(input("Enter a valid number:"))
    return sum_to(input1,0)
def sum_to(n,sum1):
    if(n==0):
        return sum1
    else:
        sum1+=n
        n-=1
        return sum_to(n,sum1)
print(third())
        
#q4 
def fourth():
    input1 = int(input("Enter a number:"))
    return square_sum_to(input1)
def square_sum_to(n):
    return (n*(n+1)*(2*n + 1))//6
print(fourth())

#q5 
def fifth():
    input1 = int(input("Enter a number:"))
    return sum_of_digits(input1)
def sum_of_digits(n):
    sum1=0
    while n>0:
        sum1+= n%10
        n=n//10
    return sum1
print(fifth())        

#q6 
def sixth():
    input1 = int(input("Enter a number:"))
    return largest_fibo(input1)
def largest_fibo(n):
    a,b=0,1
    while b<n :
        a,b=b,a+b
        if(b>n):
            return a
sixth()

#q7 
def seventh():
    input1 = int(input("Enter a number:"))
    return prime_factors(input1)
def prime_factors(n):
    numbers=[]
    while n%2==0:
        numbers.append(2)
        n=n//2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            numbers.append(i)
            n = n//i
    if n > 1:
        numbers.append(n)
    return numbers
print(seventh())

#q8 
def eighth():
    input1 = int(input("Enter a number:"))
    return prime_count(input1)
def prime_count(n):
    count=0
    for i in range(2,n):
        x = is_prime(i)
        if x:
            count+=1
        else:
            continue
    return count
def is_prime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
eighth()

#q9 
def ninth():
    input1 = int(input("Enter a number:"))
    return smallest_prime_larger_than(input1)
def smallest_prime_larger_than(n):
    while n!=0:
        x = is_prime1(n)
        if x:
            break
        else:
            n+=1
    return n
def is_prime1(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
ninth()

#q10 a
def a():
    m = int(input("Enter a number:"))
    n = int(input("Enter another number:"))
    print(multiply(m,n))
def multiply(m,n):
    if n==0:
        return 0
    else:
        return (multiply(m,n-1) + m)
a()

#q10 b
def b():
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    print(power(x,y))
def power(x,y):
    if y==0:
        return 1
    else:
        return (power(x,y-1)*x)
b()

#q10 c
def c():
    input1 = str(input("Enter a number:"))
    print(palindrome(input1))
def palindrome(s):
    if len(s) < 1:
        return "Palindrome"
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return "Not Plaindrome"
c()

#q10 d
def d():
    input1=int(input("Enter a number:"))
    input2=int(input("Enter another number:"))
    print(gcd(input1,input2))
def gcd(a,b):
    r=a%b
    if r==0:
        return b
    if r==1:
        return 1
    return gcd(b,r)
d()

#q10 e
def e():
    input1 = int(input("Enter a number:"))
    return sum_of_digits1(input1)
def sum_of_digits1(x):
    a=x%10
    if x==0:
        return 0
    x=x//10
    return sum_of_digits1(x)+a
print(e())

#q10 f
def f():
    input1 = int(input("Enter a positive number:"))
    return (dec2bin(input1))
def dec2bin(n):
    if n == 0:
        return '0'
    else:
        return dec2bin(n//2) + str(n%2)
print(f())

#q11
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

#q12
def polite_num(n):
    a=[]
    count=0
    for i in range(1,(n//2)+1):
        sum=0
        for j in range(i,(n//2)+1):
            a.append(j)
            sum+=j
            if sum>n:
                a.clear()
                break
            elif sum==n:
                print(a)
                count+=1
    if count==0:
        print(n,"is impolite number")
polite_num(32)   

#q13
def isprime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
    else:
        return 1

def twin_prime():
    for i in range(101,201):
        if isprime(i) and isprime(i+2):
            print("(",i,",",i+2,")",end=', ')

def twin_prime_first():
    c=1
    i=1
    while(c<=50):
        if isprime(i) and isprime(i+2):
            print("(",i,",",i+2,")",end=', ')
            c+=1
        i+=1
twin_prime()   
twin_prime_first()


#q14
def is_prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
    return 1

def gold(n):
    print(n,' = ',end=' ')
    for i in range(3,n,2):
        if is_prime(i)==0:
             continue
        sum=i
        for j in range(n-3,i,-2):
            if is_prime(j)==0:
             continue
            sum+=j
            if sum>n:    
                sum=i
                continue
            elif sum==n:
                print(i,'+',j,end=' = ')
            elif sum<n:
                sum=i    
                break

print(gold(200))   


#q15
def rev(n):
    a = 0
    while n>0:
        a = a*10 + n%10
        n = n//10
    return a

def differev(n):
    r=rev(n)
    return(n-r)
    
def check(n):
    if differev(n)+rev(n)==n:
        print (True)
    else:
        print(False)
        
differev(123)
check(123)

