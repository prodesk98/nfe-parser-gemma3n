from typing import Optional

from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class EnvironmentSettings(BaseSettings):
    OLLAMA_API_URL: str = getenv("OLLAMA_API_URL", "http://localhost:11434")
    OLLAMA_API_KEY: Optional[str] = getenv("OLLAMA_API_KEY")
    OLLAMA_MODEL: str = getenv("OLLAMA_MODEL", "gemma3n:e4b")


env = EnvironmentSettings()
