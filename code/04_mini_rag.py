import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Практическое задание: минимальная retrieval-модель для поиска релевантных фрагментов.

docs = pd.read_csv("data/nlp/emk_fragments_synthetic.csv")
query = "пациент с одышкой и снижением сатурации"

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs["text"])
q = vectorizer.transform([query])
scores = cosine_similarity(q, X).ravel()

docs["score"] = scores
print(docs.sort_values("score", ascending=False).head(3)[["doc_id", "text", "score"]])
