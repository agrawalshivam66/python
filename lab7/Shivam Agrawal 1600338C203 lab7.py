# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:27:23 2018

@author: Shivam-PC
"""

#Q1 program can raise exception if user entered real/float numbers
def insert(n):
  a.add(n)

a=set()
n=0
size=int(input("Enter no. of elements "))
print("Enter the value you want to add into the SET ")

for i in range(size):
    n=eval(input())
    try:
        if (type(n)==float):
            raise ValueError
        else:
            insert(n)

    except ValueError:
        print('User entered a real/float number')
        exit()

    finally:
        print(a)
        
#Q2 program can raise exception if user entered real/float or negative numbers
def isPrime(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            break
    else:
        return 1

def primes_upto(n):
    for i in range(2,n+1):
        if isPrime(i):
            primes_upto_n.add(i)
    for i in primes_upto_n:
        print(i,end=",")
    
primes_upto_n=set()
n=eval(input("Enter a Number: "))

try:
    if n<0 or type(n)!=int:
        raise ValueError

    else:
        primes_upto(n)
except ValueError:
    print("User entered a real/float number")

#Q3 For computing n! raise exception if user entered real/float or negative numbers
def calFactorial(n):
    sum=1
    while n>0:
        sum=sum*n
        n-=1
    print(sum)

n=eval(input("Enter the value of 'n' "))
try:
    if (type(n)==float or n<0):
        raise ValueError
    else:
        calFactorial(n)
except ValueError:
    print('User entered a real/float or negative number')


