from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env") # Load environment variables from .env file

from routes import base # Import the base router from routes/base.py

# Initialize FastAPI app
app = FastAPI(
    title="Mini RAG API",
    version="1.0.0",
    description="A FastAPI backend for the Retrieval-Augmented Generation application.",
)

# Register the router
app.include_router(base.base_router)
