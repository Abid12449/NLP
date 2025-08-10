#Practical usage of all things I learned
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
text = "Natural Language Processing enables computers to understand human language"
text = text.lower()
import string
text = text.translate(str.maketrans('', '', string.punctuation))
tokens = text.split()
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
processed_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Original text:")
print(text)
print("\\\\nFiltered Tokens(Stop Words Removed):")
print(filtered_tokens)
print("\\\\nProcessed Tokens(Stemmed and Lemmatized):")
print(processed_tokens)