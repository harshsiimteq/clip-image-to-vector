# Use a lightweight base image
FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime

# Set working directory
WORKDIR /app

# Copy only necessary files to avoid bloating the image
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application files
COPY . .

# Expose the API port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
