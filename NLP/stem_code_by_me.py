# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:21:11 2019

@author: Shivam-PC
"""

from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

new_text = 'Here is the perfect system for cleaning your room. First, move all of the items that do not have a proper place to the center of the room. Get rid of at least five things that you have not used within the last year. Take out all of the trash, and place all of the dirty dishes in the kitchen sink. Now find a location for each of the items you had placed in the center of the room. For any remaining items, see if you can squeeze them in under your bed or stuff them into the back of your closet. See, that was easy!'
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w), end = ' ')
    
print()

paragraph = new_text.split()
#Dictionary
for word in paragraph:
    flag = 0
    new_word = word
    for letters in word:
        new_word = new_word[:-1]
        if len(new_word) < 2:
            break
        syn=dictionary.meaning(new_word)
        if len(syn)!=0:
            flag = 1
            print(new_word, end = ' ')
            break
        else:
            flag = 0
    
    if flag == 0:
        print(word, end = ' ')
        
    
