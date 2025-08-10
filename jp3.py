import spacy
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load Japanese tokenizer
nlp = spacy.load("ja_ginza")

# Get Japanese article text from NHK
url = "https://www3.nhk.or.jp/news/html/20250809/k10014675151000.html"  # Example link
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract main text
article_paragraphs = soup.find_all("p")
text = " ".join(p.get_text() for p in article_paragraphs)

# Function to get English meaning from Jisho
def get_english_meaning(word):
    api_url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    res = requests.get(api_url)
    if res.status_code == 200:
        data = res.json()
        if data["data"]:
            senses = data["data"][0]["senses"][0]["english_definitions"]
            return ", ".join(senses)
    return "No definition found"

# Tokenize & create vocab list
vocab_data = []
doc = nlp(text)
for token in doc:
    word = token.text.strip()
    if word and word not in ["、", "。"]:  # skip punctuation
        meaning = get_english_meaning(word)
        vocab_data.append({"Word": word, "Meaning": meaning})

# Remove duplicates
seen = set()
unique_vocab = [v for v in vocab_data if not (v["Word"] in seen or seen.add(v["Word"]))]

# Save to CSV
df = pd.DataFrame(unique_vocab)
df.to_csv("news_vocab_list.csv", index=False, encoding="utf-8-sig")
print("✅ Vocabulary list saved as news_vocab_list.csv")
