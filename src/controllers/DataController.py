from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()  # Call the constructor of the BaseController
        self.size_scale = 1024 * 1024   # 1 MB in bytes
        
    def validate_uploaded_file(self, file: UploadFile):
        """
        Validate the uploaded file type and size.
        """
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        # Check if the file size exceeds the limit
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            # Convert the size to MB for the error message
            return False, ResponseSignal.FILE_SIZE_EXCEEDS.value
                
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
    
    def genertate_unique_filename(self, orign_file_name: str, project_id: str) -> str:
        """
        Generate a unique filename for the uploaded file.
        """
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        cleaned_file_name = self.get_cleaned_file_name(orign_file_name=orign_file_name)
        
        new_file_path = os.path.join(
            project_path, f"{random_key}_{cleaned_file_name}"
        )
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path, f"{random_key}_{cleaned_file_name}"
            )
        return new_file_path
            
            
    def get_cleaned_file_name(self, orign_file_name: str) -> str:
        """
        Clean the original file name by removing special characters and spaces.
        """
        # Remove special characters, except underscore and dot
        cleaned_file_name = re.sub(r'[^\w.]', '', orign_file_name.strip())
        
        # Replace spaces with underscores
        cleaned_file_name = cleaned_file_name.replace(" ", "_")
        
        return cleaned_file_name