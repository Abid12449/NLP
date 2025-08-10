#Sample Text
text = "Natural Language Processing (NLP) enables computers to understand human languages"
#Display the Text
print("Original Text")
print(text)
#length of the text
print("\\\\nLength of the text:", len(text))
#Uniqe characters in the text
unique_characters = set(text)
print("\\\\nUnique characters:", unique_characters)
#Number of words in the text
words = text.split()
print("\\\\nNumber of words:", len(words))
#Display the words
print("\\\\nWords in the text:")
print(words)
