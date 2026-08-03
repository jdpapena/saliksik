"""Define environment-based settings for SALIKSIK."""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Load application settings from environment variables."""

    app_name: str = "SALIKSIK API"
    app_version: str = "1.0.0"

    # SQLite is used locally unless a production database URL is provided.
    database_url: str = "sqlite:///./saliksik.db"

    # The SEC asks automated clients to provide identifying information.
    sec_user_agent: str = "SALIKSIK jeremiah.papena@gmail.com"

    # The frontend URL is used by the API's CORS configuration.
    frontend_url: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()