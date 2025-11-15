import os
from dotenv import load_dotenv
from transformers import pipeline

import nltk
from nltk.tokenize import sent_tokenize

# punkt 데이터 자동 설치
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

# punkt_tab 데이터 자동 설치 (NLTK 3.8+ 필수)
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HF_TRANSLATION = os.getenv("HF_TRANSLATION")

translation = pipeline("translation", model=HF_TRANSLATION)


def translate_text(text: str):
    result = translation(text)
    return (
        result[0]["translation_text"]
        if result and "translation_text" in result[0]
        else result
    )


def translate_sentences(text: str):
    sentences = sent_tokenize(text, language="english")
    results = translation(sentences)
    return [r["translation_text"] if "translation_text" in r else r for r in results]
