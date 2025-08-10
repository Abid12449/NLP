#Tokenizing Chapter
import nltk
from nltk.tokenize import word_tokenize
text = "Natural Language Processing enables computers to understand human langauge"
tokens = word_tokenize(text)
print("Word Tokenize:")
print(tokens)

import spacy
nlp = spacy.load("en_core_web_sm")
text = "Natural Language Processing enables computers to understand human langauge."
doc = nlp(text)
tokens = [token.text for token in doc]
print("Word Tokens:")
print(tokens)