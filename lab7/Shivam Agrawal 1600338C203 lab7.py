# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:27:23 2018

@author: Shivam-PC
"""
#Q1 program can raise exception if user entered real/float numbers
n = eval(input("Enter a number: "))
if  type(n) != int :
    negativeError = ValueError('Number should be positive')
    raise negativeError
print(n)
    

#Q2 program can raise exception if user entered real/float or negative numbers
n = eval(input("Enter a number: "))
if n < 0 or type(n) != int :
    negativeError = ValueError('Number should be integer and positive')
    raise negativeError
print(n)

#Q3 For computing n! raise exception if user entered real/float or negative numbers
def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

n = eval(input("Enter a number: "))
if n < 0 or type(n) != int :
    negativeError = ValueError('Number should be integer and positive')
    raise negativeError
else:
    print(factorial(n))
   
