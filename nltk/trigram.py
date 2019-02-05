# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:26:19 2019

@author: Shivam-PC
"""

def trigram(st):
    words = st.split()
    three_words = []
    two_words = []
    probability = []
    three_words_dict = dict() 
    for i in range(0, len(words)-2):
        three_words.append(words[i] + ' ' + words[i+1] + ' ' + words[i+2])
        two_words.append(words[i] + ' ' + words[i+1])
    two_words.append(words[len(words)-2] + ' ' + words[len(words)-1])
    
    for i in three_words:
        three_words_dict[i] = three_words.count(i)
        
    for i in three_words_dict:
        prob = three_words_dict[i] / two_words.count((i.split())[0] + ' ' + (i.split())[1])
        probability.append(i + ' -- ' + str(prob))
    
    for i in probability:
        print(i)

st = 'Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been'

trigram(st)