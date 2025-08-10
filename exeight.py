import nltk
import re
text = "The quick brown fox jumps over the lazy dog. The fox is clever."
pattern = r"fox"
new_text = re.sub(pattern, "cat", text)
print("Modified text:")
print(new_text)