import os
from pathlib import Path

import torch 
from torchvision import models, transforms

model = models.resnet18(pretrained=True)
model.eval()

import json

def load_german_classes():
    with open('imagenet_german/imagenet_deutsch_vollstaendig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Dictionary erstellen: Index -> deutscher Name
    translations = {}
    for item in data['uebersetzungen']:
        translations[item['index']] = item['deutsch']
    
    return translations

from PIL import Image

# Transformation für das Modell
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                        std=[0.229, 0.224, 0.225])
])

def prepare_image(image_path):
    img = Image.open(image_path).convert('RGB')
    return transform(img).unsqueeze(0)

def classify_image(image_path, model, german_classes):
    # Bild vorbereiten
    input_tensor = prepare_image(image_path)
    
    # Vorhersage
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    # Top 3 Ergebnisse
    top3 = torch.topk(probabilities, 3)
    
    print(f"Analyse von: {image_path}")
    for i in range(3):
        idx = top3.indices[i].item()
        confidence = top3.values[i].item() * 100
        german_name = german_classes.get(idx, f"Unbekannte_Klasse_{idx}")
        print(f"{i+1}. {german_name}: {confidence:.1f}%")

def find_image_files(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    image_files = []
    
    for file_path in Path(folder_path).iterdir():
        if file_path.suffix.lower() in image_extensions:
            image_files.append(str(file_path))
    
    return image_files

def analyze_all_images(folder_path, model, german_classes):
    image_files = find_image_files(folder_path)
    
    print(f"Analysiere {len(image_files)} Bilder...")
    print("=" * 50)
    
    for image_path in image_files:
        classify_image(image_path, model, german_classes)
        print("-" * 30)

def save_results_to_file(results, output_file="analysis_results.txt"):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Bilderkennung Ergebnisse\n")
        f.write("=" * 30 + "\n\n")
        
        for result in results:
            f.write(result + "\n")
    
    print(f"Ergebnisse gespeichert in: {output_file}")

german_classes = load_german_classes()
analyze_all_images("C:/Users/praktikant/Documents/Python_Praktikum/tag_03/bilder_test", model, german_classes)