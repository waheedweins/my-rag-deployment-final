import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

    @classmethod
    def validate(cls):
        if not cls.GOOGLE_API_KEY:
            raise RuntimeError("GOOGLE_API_KEY not set")
        if not cls.PINECONE_API_KEY:
            raise RuntimeError("PINECONE_API_KEY not set")
        if not cls.PINECONE_INDEX_NAME:
            raise RuntimeError("PINECONE_INDEX_NAME not set")

Settings.validate()

settings = Settings()
