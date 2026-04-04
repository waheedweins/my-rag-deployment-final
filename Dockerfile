# Use Amazon's copy of Python 3.11-slim to avoid Docker Hub rate limits
FROM public.ecr.aws/docker/library/python:3.11-slim

# Prevent Python from writing .pyc files & flush logs immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Start Gunicorn using main:app (since you renamed app.py to main.py)
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app","--timeout", "999", "--bind", "0.0.0.0:8000", "--workers", "2"]
