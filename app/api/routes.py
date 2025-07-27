from fastapi import APIRouter, Form
from app.services.rag_engine import generate_script
from app.services.chroma_manager import ingest_kb

router = APIRouter()

@router.post("/ingest_kb")
async def ingest_knowledge_base():
    return ingest_kb()

@router.post("/generate_script")
async def generate_script_route(task: str = Form(...)):
    prompt = generate_script(task)
    return {"prompt": prompt}


