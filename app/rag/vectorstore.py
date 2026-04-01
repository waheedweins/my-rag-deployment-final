from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from app.core.config import settings
from app.rag.embeddings import get_embeddings
from langchain_core.documents import Document
from typing import List

class VectorStoreService:

    def __init__(self):
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index = self.pc.Index(settings.PINECONE_INDEX_NAME)
        self.embeddings = get_embeddings()

        self.vectorstore = PineconeVectorStore(
            index=self.index,
            embedding=self.embeddings
        )

    def add_documents(self, documents: List[Document]):
        if documents:
            self.vectorstore.add_documents(documents)

    def get_retriever(self, k: int = 3):
        return self.vectorstore.as_retriever(search_kwargs={"k": k})
