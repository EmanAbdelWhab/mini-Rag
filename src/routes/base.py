from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings

# Define API router with versioned prefix and tag
base_router = APIRouter(
    prefix="/api/v1",
    tags=["API_v1"],
)

# Root route of the API
@base_router.get("/")
async def welcome(app_settings=Depends(get_settings)):

    app_name =app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version,
        }
