# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:03:13 2018

@author: Shivam-PC
"""

cfile = open('sfile.cpp','r')
lines=''

#Reading all the lines and saving it
for i in cfile: 
    lines += i

#reading all the characters/words in lines and saving it
words = lines.split()

#Some common operators in C language  
operators = ['int','main',	'('	,')','[',']','if','else','<',';','for','=','-','<=','++','printf','{','}',',','auto', 'break',	'case','char','while', 'continue','double','char']

operators_present=dict()
operands_present=dict()

#counting number of occurance of each and checking weather it is operator or operand 
for j in words:
    if j in operators:
        operators_present[j] = words.count(j)
    else:
        operands_present[j] = words.count(j)
        
#deleting extra brackets 
operators_present["{ }"] = operators_present.get('{')
operators_present["()"] = operators_present.get('(')

brackets = ['(',')','{','}','[',']']
for i in brackets:
    if i in operators_present:
        operators_present.pop(i)

# Calclulating N1 and N2
N1 = len(operators_present)
N2=0
for i in operators_present:
    N2 += operators_present.get(i)

# Calclulating n1 and n2
n1 = len(operands_present)
n2=0
for i in operands_present:
    n2 += operands_present.get(i)




            