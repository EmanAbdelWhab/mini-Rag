from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal

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