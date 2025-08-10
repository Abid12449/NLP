import nltk
from nltk import WordNetLemmatizer
text = "Natural Language Processing (NLP) enables computers to understand human languages"
#Tokenize
tokens = text.split()
#Lemmatization initialise
lemmatizer = WordNetLemmatizer()
#Lemmatize tokens
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
print("Original Text:")
print(tokens)
print("\\\\nLemmatized Tokens:")
print(lemmatized_tokens)
