from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.rag.vectorstore import VectorStoreService
from app.rag.chain import create_rag_chain

app = FastAPI(title="Production Pinecone RAG API")

# Add CORS Middleware to allow browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    vector_service = VectorStoreService()
    retriever = vector_service.get_retriever(k=3)
    app.state.rag_chain = create_rag_chain(retriever)

app.include_router(router)
