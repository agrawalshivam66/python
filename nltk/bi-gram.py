# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:22:35 2019

@author: Shivam-PC
"""


def bigram(st):
    words = st.split()
    two_words = []
    words_dict = dict()
    probability = []
    
    for i in range(0, len(words)-1):
        two_words.append(words[i] + ' ' + words[i+1])
    
    for i in two_words:
        words_dict[i] = two_words.count(i)
        
    for i in words_dict:
        prob = words_dict[i] / words.count((i.split())[0])
        probability.append(i + ' -- ' + str(prob))
    
    for i in probability:
        print(i)
        
        
st = 'Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been'
bigram(st)

