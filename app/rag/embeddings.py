from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=settings.GOOGLE_API_KEY,
        output_dimensionality=768
    )
