import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


nlp = spacy.load("en_core_web_sm")

def summarize(text, n=3):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    if len(sentences) <= n:
        return sentences

    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(sentences)
    scores = np.array(X.sum(axis=1)).flatten()

    top_n_idx = scores.argsort()[-n:][::-1]
    summary = [sentences[i] for i in sorted(top_n_idx)]

    return summary
