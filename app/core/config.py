from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@db/messenger"

    class Config:
        env_file = ".env"
        extra = "allow"  # Разрешаем дополнительные поля в конфигурации

settings = Settings()
