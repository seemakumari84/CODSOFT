import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained ResNet model for image feature extraction
resnet = models.resnet50(pretrained=True)
resnet = nn.Sequential(*list(resnet.children())[:-1])  # Remove the last classification layer
resnet.eval()

# Preprocessing pipeline for the images
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def extract_features(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    image = preprocess(image).unsqueeze(0)
    
    # Extract features using ResNet
    with torch.no_grad():
        features = resnet(image)
    return features.squeeze()

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

def generate_caption(features):
    # Convert features to text input (this is a placeholder, as GPT-2 expects text input)
    # You might need to use a more sophisticated approach to convert features to a meaningful input for GPT-2
    input_text = "This image shows"
    
    # Tokenize and generate caption
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    
    caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption

def caption_image(image_path):
    features = extract_features(image_path)
    caption = generate_caption(features)
    return caption

# Test the function with an example image
image_path = "content.jpg"
caption = caption_image(image_path)
print("Caption:", caption)
