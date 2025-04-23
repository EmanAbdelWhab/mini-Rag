from fastapi import FastAPI
from routes import base # Import the base router from routes/base.py
from routes import data # Import the data router from routes/data.py

# Initialize FastAPI app
app = FastAPI(
    title="Mini RAG API",
    version="1.0.0",
    description="A FastAPI backend for the Retrieval-Augmented Generation application.",
)

# Register the router
app.include_router(base.base_router)
app.include_router(data.data_router)