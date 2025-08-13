#remove stopwords
import nltk
from nltk.corpus import stopwords
text = "NLP allows computers to understand human language, which is a crucial aspect of artificial intelligence."
#tokenize
tokens = text.split()
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Original text:")
print(tokens)
print("Filtered Tokens:")
print(filtered_tokens)

#stemming
from nltk.stem import PorterStemmer
text = "Stemming helps to reduce words to their root forms, which can be benficial for text procesing."
tokens = text.split()
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
print("Original Tokens:")
print(tokens)
print("Stemmed Tokens:")
print(stemmed_tokens)

#Lemmatization
from nltk.stem import WordNetLemmatizer
text = "Lemmatization is the process of reducing words to their base or root form"
tokens = text.split()
lemmatizer = WordNetLemmatizer()
lemmatoze_tokens = [lemmatizer.lemmatize(word) for word in tokens]
print("Original Tokens:")
print(tokens)
print("Lemmatized Tokens:")
print(lemmatoze_tokens)

#Regular Expressions
import re
text = "The project started on 2021-01-15 and ended on 2021-12-31"
pattern = r"\b\d{4}-\d{2}-\d{2}\b"
dates = re.findall(pattern, text)
print("Find Dates:")
print(dates)

#Word Tokennization
from nltk.tokenize import word_tokenize
text = "Tokenization is the first step in text processing."
tokens = word_tokenize(text)
print("Word Tokenize:")
print(tokens)

#Sentence Tokenize
from nltk.tokenize import sent_tokenize
text = "Tokenization is essential. It breaks down text into smaller units"
tokens = sent_tokenize(text)
print("Original Sentence:")
print(tokens)