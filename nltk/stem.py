from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."


for w in example_words:
    print(ps.stem(w))
    
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
