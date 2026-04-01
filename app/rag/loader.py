import boto3
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List

def download_from_s3(bucket: str, key: str, download_path: str):
    s3 = boto3.client("s3")
    s3.download_file(bucket, key, download_path)

def load_documents_from_s3(bucket: str, key: str) -> List[Document]:
    local_path = f"/tmp/{key}"

    download_from_s3(bucket, key, local_path)

    loader = PyPDFLoader(local_path)
    return loader.load()
