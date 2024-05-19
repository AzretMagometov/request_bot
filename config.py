from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str
    admins: list[int]
    DB_URL: str = 'sqlite+aiosqlite:///db.sqlite3'

    class Config:
        env_file = '.env'


def create_settings() -> Settings:
    return Settings()
