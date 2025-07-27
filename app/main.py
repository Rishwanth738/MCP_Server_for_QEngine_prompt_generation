from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="QEngine MCP Server",
    description="Injects QEngine KB into prompts using RAG",
    version="1.0"
)

app.include_router(router)
