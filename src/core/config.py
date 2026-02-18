from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='.env', extra='ignore')

  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  POSTGRES_HOST: str
  POSTGRES_PORT: int
  POSTGRES_DB: str     
  
settings = Settings()