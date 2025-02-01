import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, num_keywords=10):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return [word for word, _ in Counter(keywords).most_common(num_keywords)]

if __name__ == "__main__":
    sample_text = "Machine learning is a field of artificial intelligence that focuses on developing algorithms that learn from data."
    print("Key Concepts:", extract_keywords(sample_text))
