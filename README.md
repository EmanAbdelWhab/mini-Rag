# 🧠 RAG (Retrieval-Augmented Generation) Model

This is an implementation of the **RAG (Retrieval-Augmented Generation)** model for answering questions based on a custom knowledge base. The model integrates a retriever and a generator to provide contextually enriched responses using both neural search and language generation.

# Requirements
- Python 3.8 or later

## Run the FastAPI server

```bash
uvicorn main:app -- reload --host 0.0.0.0 -- port 5000
```
or

```bash
fastapi dev main.pu
```