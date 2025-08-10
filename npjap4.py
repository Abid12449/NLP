import streamlit as st
import spacy
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Load Japanese model once
@st.cache_resource
def load_model():
    return spacy.load("ja_ginza")

nlp = load_model()

# Function to get English meaning from Jisho
@st.cache_data
def get_english_meaning(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if data["data"]:
            senses = data["data"][0]["senses"][0]["english_definitions"]
            return ", ".join(senses)
    return "No definition found"

# Function to scrape article text
def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join(p.get_text() for p in paragraphs)

# Streamlit UI
st.title("📚 Japanese Vocab List Generator")
st.write("Paste Japanese text or a news article URL to get an English gloss list.")

input_type = st.radio("Choose input type:", ["Text", "URL"])

if input_type == "Text":
    jp_text = st.text_area("Enter Japanese text here:")
elif input_type == "URL":
    article_url = st.text_input("Enter article URL:")
    if article_url:
        jp_text = get_article_text(article_url)
        st.write("### Extracted Text:")
        st.write(jp_text)
    else:
        jp_text = ""

if st.button("Generate Vocabulary List") and jp_text.strip():
    doc = nlp(jp_text)
    vocab_data = []
    for token in doc:
        word = token.text.strip()
        if word and word not in ["、", "。"]:
            meaning = get_english_meaning(word)
            vocab_data.append({"Word": word, "Meaning": meaning})

    seen = set()
    unique_vocab = [v for v in vocab_data if not (v["Word"] in seen or seen.add(v["Word"]))]

    df = pd.DataFrame(unique_vocab)
    st.dataframe(df)

    csv = df.to_csv(index=False, encoding="utf-8-sig")
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="vocab_list.csv",
        mime="text/csv"
    )
