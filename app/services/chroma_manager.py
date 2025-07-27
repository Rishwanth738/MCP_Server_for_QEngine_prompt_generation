import chromadb
from app.utils.md_parser import parse_all_markdowns

client = chromadb.Client()
collection = client.get_or_create_collection(name="qengine_kb")

def ingest_kb():
    docs = parse_all_markdowns()
    collection.add(
        documents=[doc["text"] for doc in docs],
        metadatas=[doc["meta"] for doc in docs],
        ids=[f"id_{i}" for i in range(len(docs))]
    )
    return {"status": "ingested", "chunks": len(docs)}
