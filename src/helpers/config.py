from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application configuration loaded from environment variables or .env file."""

    # Define the settings with their types and default values

    APP_NAME : str 
    APP_VERSION : str
    openai_api_key : str
    
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    
    FILE_DEFAULT_CHUNK_SIZE : int
    class Config:
        """Configuration for the settings."""
        env_file = ".env"
        
def get_settings() -> Settings:
    """Get the application settings."""
    return Settings()
    