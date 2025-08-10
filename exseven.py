import re
text =  "The quick brown fox jumps over the lazy dog."
#pattern to search fox
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print("Match Found:", match.group())
else:
    print("No match found.")
#Email Extraction
text = "Please contact us at support@example.com or sales@example.com for further information"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text, re.IGNORECASE)
print("Extracted Email Addresses:")
print(emails)
import re
text = "Contact us at (123) 456-7890 or (987) 654-3210"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
phone_numbers = re.findall(pattern, text, re.IGNORECASE)
print("Extracted Phone Numbers:")
print(phone_numbers)
