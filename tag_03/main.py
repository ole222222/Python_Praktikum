import torch 
from torchvision import models , transforms

# Vortrainiertes ResNet18 Modell laden
model = models.resnet18(pretrained=True)
model.eval()  

#Deutsche Klassen laden:
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

# 4. Bild klassifizieren
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