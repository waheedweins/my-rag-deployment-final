import os
import sys
import logging
from app.rag.loader import load_documents_from_s3
from app.rag.splitter import split_documents
from app.rag.vectorstore import VectorStoreService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_ingestion():
    # Pulling names from environment variables to ensure consistency across ECS and S3
    bucket_name = os.getenv("S3_BUCKET_NAME", "rag-api-deployment")
    file_key = os.getenv("S3_FILE_KEY", "leave.pdf")
    
    logger.info(f"Starting ingestion: Bucket={bucket_name}, Key={file_key}")

    try:
        # Pass the variables to ensure the loader uses the correct bucket and file
        docs = load_documents_from_s3(bucket=bucket_name, key=file_key)
        
        if not docs:
            logger.error("No documents found. Check S3 bucket name and file key.")
            return

        split_docs = split_documents(docs)
        logger.info(f"Documents split into {len(split_docs)} chunks.")

        vector_service = VectorStoreService()
        vector_service.add_documents(split_docs)

        logger.info("Ingestion successful. Pinecone index updated.")

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_ingestion()
