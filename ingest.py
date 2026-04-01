from app.rag.loader import load_documents_from_s3
from app.rag.splitter import split_documents
from app.rag.vectorstore import VectorStoreService

def run_ingestion():
    print("Downloading and loading documents from S3...")

    docs = load_documents_from_s3(
        bucket="rag-api-deployment",
        key="leave.pdf"
    )

    split_docs = split_documents(docs)

    print(f"Split into {len(split_docs)} chunks")

    vector_service = VectorStoreService()
    vector_service.add_documents(split_docs)

    print("Ingestion completed successfully.")

if __name__ == "__main__":
    run_ingestion()
