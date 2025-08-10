import nltk
from nltk.corpus import stopwords
text = "Natural Language Processing (NLP) enables computers to understand human languages"
tokens = text.split()
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Original Tokens:")
print(tokens)
print("\\\\nFiltered Tokens:")
print(filtered_tokens)

#Stemming Words
from nltk.stem import PorterStemmer
text = "Natural Language Processing (NLP) enables computers to understand human languages"
tokens = text.split()
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
print("Original Tokens:")
print(tokens)
print("\\\\nStemmed Tokens:")
print(stemmed_tokens)