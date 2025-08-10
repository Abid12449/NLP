import nltk
import re
text = "The event is scheduled for 2022-08-15. Another event is on 15/08/2022."
pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b"
dates = re.findall(pattern, text)
print("Extracted Dates:")
print(dates)

text = "Loving the new features of this product! #excited #newrelease #tech"
pattern = r"#\w+"
hastags = re.findall(pattern, text)
print("Extracted Hashtags:")
print(hastags)