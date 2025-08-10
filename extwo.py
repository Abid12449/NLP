text = "Natural Language Processing (NLP) enables computers to understand human languages"
text = text.lower()
print("Lower Text:")
print(text)
import string
text = text.translate(str.maketrans('', '', string.punctuation))
print("\\\\nText withoiut Punctuation:")
print(text)
#Tokenize text
tokens = text.split()
print("\\\\nTokens:")
print(tokens)