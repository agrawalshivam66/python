# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 19:05:41 2018

@author: Shivam-PC
"""

a = [3,4,1,0,2,0,1,1]
#a=[2,2,0,0,2,0,1,1]
max=0
b=[]
b.append(0)
m=0
while m < len(a)-1:
    
    for j in range(m,m+a[m]+1):
        if(a[j]+j > max):
            max=a[j]+j
            m=j
            flag=1
            
    if flag==0:
        print("no")
        break
    
    b.append(m)
    flag=0

if m>=len(a)-1:
    print("yes")
    print(b)
    