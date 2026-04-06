import os
import anthropic
import chromadb
from sentence_transformers import SentenceTransformer

filename = input("Which file do you want to query?: ")

with open(filename, "r") as f:
    text = f.read()

chunks = [chunk.strip() for chunk in text.split("---") if chunk.strip()]

print("Creating embeddings...")
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks).tolist()

client = chromadb.Client()
collection = client.get_or_create_collection("docs")
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)
print(f"Stored {len(chunks)} chunks in vector database")

question = input("\nAsk a question: ")

question_embedding = model.encode([question]).tolist()
results = collection.query(query_embeddings=question_embedding, n_results=2)
relevant_chunks = "\n\n".join(results["documents"][0])

anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
message = anthropic_client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": f"Based on this context:\n\n{relevant_chunks}\n\nAnswer this question: {question}"}]
)

print("\nAnswer:", message.content[0].text)
