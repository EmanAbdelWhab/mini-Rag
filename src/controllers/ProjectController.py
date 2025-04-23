from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()  # Call the constructor of the BaseController
        
    def get_project_path(self, project_id: str) -> str:
        """
        Get the project path for a given project ID.
        """
        project_dir = os.path.join(
            self.files_dir, project_id
            )
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        return project_dir