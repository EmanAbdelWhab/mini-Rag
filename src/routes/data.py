from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, Settings

data_router = APIRouter(
    prefix="/api/vi/data",
    tags=["API_v1","Data"],
)

@data_router.post("/upload/{project_id}") # tenaintionally not using /api/v1/data/upload/{project_id} to avoid confusion with the base router
async def upload_data(project_id: str, file: UploadFile ,
                    app_settings: Settings = Depends(get_settings)):
    """
    Upload data to the server for a specific project.
    """
