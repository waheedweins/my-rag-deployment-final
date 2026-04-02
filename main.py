from fastapi import FastAPI
from app.api.router import router
from app.rag.vectorstore import VectorStoreService
from app.rag.chain import create_rag_chain

app = FastAPI(title="Production Pinecone RAG API")

@app.on_event("startup")
def startup():
    vector_service = VectorStoreService()
    retriever = vector_service.get_retriever(k=3)
    app.state.rag_chain = create_rag_chain(retriever)

# Register router
app.include_router(router)
