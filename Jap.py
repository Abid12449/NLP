import spacy
import requests

# Load Japanese model
nlp = spacy.load("ja_ginza")

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
text = "私は昨日、東京で美味しい寿司を食べました。"
doc = nlp(text)

for token in doc:
    if token.text.strip():  # skip empty tokens
        meaning = get_english_meaning(token.text)
        print(f"{token.text} → {meaning}")
