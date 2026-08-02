"""Application settings loaded from environment variables."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    twelve_data_api_key: str = ""

    # SEC asks automated clients to identify themselves.
    sec_user_agent: str = "SALIKSIK jeremiah.papena@gmail.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()