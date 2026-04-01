# Use lightweight Python 3.11 image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & flush logs immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for some packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Production-ready command using Gunicorn + Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2"]
