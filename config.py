from pydantic_settings import BaseSettings
from enum import Enum
from functools import lru_cache

class Profile(str, Enum):
    STAGING = "staging"
    PRODUCTION = "production"

class ProfileSetting(BaseSettings): # type: ignore
    profile: Profile

    def get_settings(self):
        return Settings(_env_file="src/environments/.env" + "." + self.profile.lower()) # type: ignore

    class Config:
        env_file = "src/environments/.env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings): # type: ignore
    AWS_S3_ACCESS_KEY: str
    AWS_S3_SECRET_KEY: str
    AWS_S3_BUCKET_NAME: str
    AWS_S3_DATASET_FILENAME: str
    AWS_S3_MEDICATIONS_BUCKET_NAME: str
    AWS_S3_MEDICATIONS_DATASET_FILENAME: str
    AWS_S3_INDIAN_MEDICAL_INDEX_FILENAME: str
    OPENAI_API_KEY: str
    OPENAI_EMBEDDING_MODEL: str
    LLM1_BASE_URL:str
    LLM2_BASE_URL:str
    LLM1_MODEL_NAME:str
    LLM2_MODEL_NAME:str
    OPENAI_MODEL_NAME:str
    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    profile = ProfileSetting() # type: ignore
    return profile.get_settings()