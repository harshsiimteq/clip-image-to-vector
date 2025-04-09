# Use a lightweight base image
FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime

# Set working directory
WORKDIR /app

# Install git before installing Python packages
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy only necessary files to avoid bloating the image
COPY /app /app

# Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# Ensure correct permissions
RUN chmod +x /app

# Expose the API port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
