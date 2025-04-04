from fastapi import FastAPI, File, UploadFile
from PIL import Image
import torch
import torchvision.transforms as transforms
import io
import uvicorn

app = FastAPI()

# Load ResNet-50 model
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=True)
model.eval()  # Set model to evaluation mode

# Image transformation function
transform = transforms.Compose([
    transforms.ToTensor()
])

@app.post("/convert-image-to-vector")
async def convert_image(file: UploadFile = File(...)):
    """Convert an uploaded image to a feature vector."""
    try:
        # Read the image file
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")

        # Transform and add batch dimension
        img_tensor = transform(image).unsqueeze(0)

        # Extract vector
        with torch.no_grad():
            vector = model(img_tensor).squeeze().numpy().tolist()

        return {"filename": file.filename, "vector": vector}

    except Exception as e:
        return {"error": str(e)}


# Run FastAPI on port 8090
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
