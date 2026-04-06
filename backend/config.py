from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://aft_user:secure_password@postgres:5432/aft_db"
    REDIS_URL: str = "redis://redis:6379/0"
    SECRET_KEY: str = "change_me_in_production"
    BACKEND_PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
