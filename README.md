# MCP_Server_for_QEngine_Prompt_Generation

## Overview

This project was built during my internship at **Zoho**. It exposes an MCP-compatible FastAPI server to ingest markdown-based knowledge bases and generate QEngine-ready prompts for LLMs hosted on **Open WebUI** to generate QEngine test scripts based on custom functions defined in the .md knowledge base.

---

## Features

- `/ingest_kb`: Ingests structured markdown content into ChromaDB as embeddings.
- `/generate_script`: Dynamically generates context-aware QEngine scripts from user prompts using custom functions and templates.

---

## Stack

- **FastAPI** - Web server and API routing  
- **ChromaDB** - Vector DB for RAG pipeline  
- **Sentence Transformers** - Embedding models for semantic search  
- **Markdown Parser** - Converts `.md` knowledge files to vector chunks

---

## Getting Started

```bash
git clone https://github.com/Rishwanth738/MCP_Server_for_QEngine_prompt_generation.git
cd MCP_Server_for_QEngine_prompt_generation
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Example Usage
```
curl -X POST http://localhost:8000/ingest_kb

curl -X POST "http://localhost:8000/generate_script" ^
     -H "Content-Type: application/x-www-form-urlencoded" ^
     -d "task=your_task_here"
```

Knowledge Base
Located in the /data folder:
ADD YOUR .md files here

