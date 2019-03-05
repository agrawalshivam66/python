from nltk.corpus import wordnet
 
word = str(input("Enter the word "))
syn=wordnet.synsets(word)
print(syn[0].definition())
print(syn[0].examples())
