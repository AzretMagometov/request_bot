from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str
    admins: list

    class Config:
        env_file = '.env'


settings = Settings()
