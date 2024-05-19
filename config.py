from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    token: str
    admins: list[int]

    class Config:
        env_file = '.env'


def create_settings() -> Settings:
    return Settings()
