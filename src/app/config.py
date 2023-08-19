from pydantic_settings import BaseSettings


class Config(BaseSettings):
    token: str

    class Config:
        env_nested_delimiter = '_'
