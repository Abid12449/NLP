import spacy
import requests
import pandas as pd

# Load Japanese model
nlp = spacy.load("ja_ginza")

# Function to get English meaning from Jisho
def get_english_meaning(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            senses = data["data"][0]["senses"][0]["english_definitions"]
            return ", ".join(senses)
    return "No definition found"

# Sample Japanese text
text = "私は昨日、東京で美味しい寿司を食べました。昨日の天気も良かったです。"
doc = nlp(text)

# Create vocabulary list
vocab_data = []
for token in doc:
    word = token.text.strip()
    if word and word not in ["、", "。"]:  # skip punctuation
        meaning = get_english_meaning(word)
        vocab_data.append({"Word": word, "Meaning": meaning})

# Remove duplicates while keeping order
seen = set()
unique_vocab = [v for v in vocab_data if not (v["Word"] in seen or seen.add(v["Word"]))]

# Create DataFrame
df = pd.DataFrame(unique_vocab)

# Save to CSV
df.to_csv("vocab_list.csv", index=False, encoding="utf-8-sig")

print("✅ Vocabulary list saved as vocab_list.csv")
