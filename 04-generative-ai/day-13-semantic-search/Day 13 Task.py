import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#Documents
df = pd.read_csv("bbc-news-data.csv", sep="\t")
documents = df["content"].head(50).tolist()
print("Number of documents:", len(documents))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents)
print("Embedding shape:", embeddings.shape)

# User query
#query = input("Enter your query: ")
query = "How is technology changing the world?"

# Create query embedding
query_embedding = model.encode([query])
print("Query embedding shape:", query_embedding.shape)

# Calculate similarity
similarities = cosine_similarity(query_embedding, embeddings)[0]

# Get top 5 documents
top_indices = similarities.argsort()[-5:][::-1]

# Display results
print("\nTop Relevant Documents:\n")

for rank, i in enumerate(top_indices, start=1):
    print(f"Rank {rank}")
    print(f"Similarity Score: {similarities[i]:.4f}")
    print(f"Document: {documents[i][:500]}")
    print("-" * 80)