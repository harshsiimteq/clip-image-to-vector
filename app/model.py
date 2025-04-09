import open_clip as open_clip
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model, _, preprocess = open_clip.create_model_and_transforms(
    model_name="ViT-B-32",
    pretrained="openai",
    device=device
)

tokenizer = open_clip.get_tokenizer("ViT-B-32")
