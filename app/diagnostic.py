# diagnostic.py
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="qengine_kb")

results = collection.get()

print(f"\nTotal Chunks: {len(results['documents'])}")
for i, doc in enumerate(results['documents']):
    print(f"\n--- Chunk {i+1} ---\n{doc[:300]}")
