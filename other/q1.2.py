# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:27:34 2018

@author: Shivam-PC
"""

import math
s= str(input(""))
s=s.replace(" ","")

#print(l)
row=math.floor(math.sqrt(len(s)))
column=math.ceil(math.sqrt(len(s)))
#print (row,column)
r=[]
c1=0
a=''
for i in range(0,row):
    c2=c1+column
    a=s[c1:c2]
    c1=c2
    r.append(a)     
print(r)

msg=''
even=''
odd=''
for i in r:
    for j in range(1,len(i)+1):
        if j%2==0:
            even=even+i[j-1]
        else:
            odd=odd+i[j-1]
    msg=msg+odd+even+' '
    odd=''
    even=''

print(msg)