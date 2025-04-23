from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController

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
    is_valid, message = DataController().validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "success": False,
                "message": message,
                "project_id": project_id
            }
        )
    return {
        "success": is_valid,
        "message": message,
        "project_id": project_id
    }