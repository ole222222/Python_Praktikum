

import gradio as gr
from PIL import Image
import torch 
from torchvision import models, transforms

model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                        std=[0.229, 0.224, 0.225])
])

import json

def load_german_classes():
    with open('imagenet_german/imagenet_deutsch_vollstaendig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Dictionary erstellen: Index -> deutscher Name
    translations = {}
    for item in data['uebersetzungen']:
        translations[item['index']] = item['deutsch']
    
    return translations

def analyze_image_for_web(image):

    print("analyse image 01")
    if image is None:
        return "Kein Bild ausgewählt!"
    
    input_tensor = image
    print("input wurde angegeben")
    input_tensor = transform(image).unsqueeze(0)
    print(image)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
    print("Vorhersage erfolgreich")
    
    top3 = torch.topk(probabilities, 3)


    print("Top 3 wurden angegeben")
    # Schöne Markdown-Ausgabe erstellen
    result = "## KI-Analyse Ergebnis\n\n"
    result += "**Top 3 Erkennungen:**\n\n"

    for i in range(3):
        idx = top3.indices[i].item()
        confidence = top3.values[i].item() * 100
        german_classes = load_german_classes()
        german_name = german_classes.get(idx, f"Unbekannte_Klasse_{idx}")
        result += f"{i+1}. {german_name}: {confidence:.1f}%\n"
    
    print("analyse fertig")
    return result
# Web-Interface erstellen
interface = gr.Interface(
    fn=analyze_image_for_web,
    inputs=gr.Image(sources=["webcam", "upload"], type="pil"),
    outputs=[gr.Textbox(label="greeting", lines=3)],
    title="KI-Bilderkennung mit deutschen Namen"
)

if __name__ == "__main__":
    interface.launch(inbrowser=True, server_port=7860)