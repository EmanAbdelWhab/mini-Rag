from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import os
import aiofiles
from models import ResponseSignal
import logging

logger = logging.getLogger('uvicorn.error')
from fastapi import APIRouter, Depends, UploadFile, status


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["API_v1","Data"],
)

@data_router.post("/upload/{project_id}") # tenaintionally not using /api/v1/data/upload/{project_id} to avoid confusion with the base router
async def upload_data(project_id: str, file: UploadFile ,
                    app_settings: Settings = Depends(get_settings)):
    """
    Upload data to the server for a specific project.
    """
    data_Controller = DataController()
    is_valid, message = data_Controller.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": message,
                "project_id": project_id
            }
        )
        
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_Controller.genertate_unique_filename(
        orign_file_name=file.filename,
        project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        
        logger.error(f"Error while uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": ResponseSignal.FILE_UPLOAD_FAILED.value,
                "project_id": project_id
            }
        )
            
    return {
        "success": is_valid,
        "message": message,
        "project_id": project_id
    }