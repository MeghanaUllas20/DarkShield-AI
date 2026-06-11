import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "DarkShield AI"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    
    # Read as a simple string to avoid Pydantic V2 parsing errors
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    # Pydantic V2 uses model_config instead of class Config
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()