import nltk
text = "Natural Language Processing"
characters = list(text)
print(characters)

import nltk
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Natural Language Processing enables computers to understand human languages. It is a fascinating field."
#word tokenization
word_tokenization = nltk.word_tokenize(text)
print("Word Tokens:")
print(word_tokenization)
#Sentence Tokenization
sentence_tokenization = nltk.sent_tokenize(text)
print("Sentence Tokens:")
print(sentence_tokenization)
#use spacy
doc = nlp(text)
spacy_sentence_tokens = [sent.text for sent in doc]
print("Spacy Tokens:")
print(spacy_sentence_tokens)
#character tokens
character_tokens = list(text)
print(character_tokens)