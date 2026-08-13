from pydantic import DirectoryPath, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignores other random env variables not defined here
    )
    
    LOCAL_DATA: DirectoryPath = Field(
        default="/mock", 
        validation_alias="LOCAL_DATA"
    )
    

# Instantiate the settings object
settings = Settings()