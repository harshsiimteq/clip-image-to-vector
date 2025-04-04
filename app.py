from fastapi import FastAPI
import clip
import torch

app = FastAPI()

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

@app.get('/')
def index():
    return {
        "message": "Hello world"
    }


@app.post('/img-to-vector')
def to_vector():
    return {
        "message": "ok"
    }
