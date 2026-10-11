from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
import ollama

#Load document
with open(Path(__file__).with_name("company_knowledge.txt"), "r", encoding="utf-8") as f:
    document = f.read()
#print(document)

#Chunking
chunks = document.split("\n\n")
#print("\nChunks:")
#for chunk in chunks:
#    print("-----")
#    print(chunk)

#Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)
#print(embeddings.shape)

#Creating vector database
client = chromadb.Client()
collection = client.create_collection(name="company_knowledge")

#Storing chunks and embeddings 
collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[str(i) for i in range(len(chunks))]
)

#Querying
question = input("\nAsk a question: ")

#embedding the question
question_embedding = model.encode([question])

#Performing a similarity search
results = collection.query(
    query_embeddings=question_embedding.tolist(),
    n_results=3
)

#Get relevant context
context = "\n\n".join(results["documents"][0])
print("\nRelevant context:")
print(context)

#Connecting to LLM
response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": f"""
Answer the user's question using only the context provided below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I couldn't find that information in the company documents."
"""
        }
    ]
)

answer = response["message"]["content"]

print("\nAnswer:")
print(answer)
