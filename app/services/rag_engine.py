import chromadb
from sentence_transformers import SentenceTransformer
from app.utils.prompt_templates import generate_prompt

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection(name="qengine_kb")

def generate_script(task: str) -> str:
    task_embedding = embedding_model.encode([task])[0]

    results = collection.query(
        query_embeddings=[task_embedding],
        n_results=10
    )

    documents = results.get("documents", [[]])[0]

    print("\n=== MATCHED DOCUMENTS ===")
    for doc in documents:
        print(doc[:100], "\n---")

    if not documents:
        return "[RAG] No matching documents found."

    return generate_prompt(task, documents)
