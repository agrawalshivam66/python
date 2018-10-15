# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:51:29 2018

@author: Shivam-PC
"""

def eleven():
    r = int(input("enter the number of rows "))
    c = int(input("enter the number of columns "))
    a=[]
    for i in range(0,r):
        l=[]
        for j in range(0,c):
            x = int(input("enter the number "))
            l.append(x)
        a.append(l)
    print(a)
    
    

    for i in range(0,r):
        for j in range(0,c):
            
eleven()