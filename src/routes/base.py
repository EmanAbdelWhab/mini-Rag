from fastapi import APIRouter
import os

# Define API router with versioned prefix and tag
base_router = APIRouter(
    prefix="/api/v1",
    tags=["API_v1"],
)

# Root route of the API
@base_router.get("/")
async def welcome():
    app_name =os.getenv("APP_NAME")
    app_version = os.getenv("App_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version,
        }
