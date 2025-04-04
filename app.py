from fastapi import FastAPI, File, UploadFile
import clip
import torch
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)


def extract_image_vector(image):
    image = preprocess(image).unsqueeze(0).to(device)  # Preprocess & add batch dim
    with torch.no_grad():
        features = model.encode_image(image)
    return features.cpu().numpy().astype(np.float32).tolist()[0]


@app.get('/')
def index():
    return {
        "message": "Hello world"
    }


@app.post('/img-to-vector')
async def to_vector(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")

    try:
        vector = extract_image_vector(image)
        return {
            "vector": vector
        }
    except Exception as e:
        return {
            "error": str(e)
        }
