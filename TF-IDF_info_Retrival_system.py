from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "The cat sat on the mat",
    "The dog chased the cat",
    "The mat was on the floor"
]

query = "cat and dog"

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])
cos_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

print("Document scores:")
for i, score in enumerate(cos_sim[0]):
    print(f"Doc {i+1}: {score:.4f}")
