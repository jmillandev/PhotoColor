from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    DATABASE_URI: str
    ENVIROMENT: str = "production"


settings = Settings()  # type: ignore[call-arg]
