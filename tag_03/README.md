# Tag 3: Deep Learning mit PyTorch - Bilderkennung

## Was du heute lernst

Heute lernst du die Grundlagen von Deep Learning kennen und entwickelst eigene KI-Anwendungen für Bilderkennung - von einfachen Kommandozeilen-Tools bis hin zu modernen Web-GUIs.

## Installation und Vorbereitung

### Benötigte Pakete installieren

```bash
pip install torch torchvision pillow matplotlib requests gradio
```

**Was wird installiert:**

- `torch` - PyTorch Deep Learning Framework
- `torchvision` - Computer Vision Modelle und Transformationen
- `pillow` - Bildverarbeitung (PIL)
- `matplotlib` - Diagramme und Visualisierungen
- `requests` - HTTP-Anfragen für Klassennamen
- `gradio` - Web-GUI Framework

### Überprüfung der Installation

```python
import torch
import torchvision
import gradio as gr
from PIL import Image
import matplotlib.pyplot as plt

print("✅ Alle Pakete erfolgreich installiert!")
print(f"PyTorch Version: {torch.__version__}")
print(f"Gradio Version: {gr.__version__}")
```

## Aufgabe 1: Bilderkennung mit ResNet18 (Grundlagen)

### Ziel

Verstehe die Grundlagen von Deep Learning und nutze ein vortrainiertes ResNet18-Modell für Bilderkennung.

### Code-Snippets

#### 1. Modell laden

```python
import torch
from torchvision import models, transforms

# ResNet18 laden
model = models.resnet18(pretrained=True)
model.eval()
```

#### 2. Deutsche Klassennamen laden

```python
import json

def load_german_classes():
    """Lädt deutsche ImageNet-Klassennamen"""
    with open('imagenet_german/imagenet_deutsch_vollstaendig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Dictionary für schnelle Übersetzung erstellen
    translations = {}
    for item in data['uebersetzungen']:
        translations[item['index']] = item['deutsch']
    
    return translations

german_classes = load_german_classes()
```

#### 3. Bild klassifizieren

```python
def classify_image(image_path):
    # Bild laden und transformieren
    img = Image.open(image_path).convert('RGB')
    input_tensor = transform(img).unsqueeze(0)
    
    # Vorhersage
    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.nn.functional.softmax(output[0], dim=0)
    
    # Top-5 mit deutschen Namen
    top5 = torch.topk(probs, 5)
    for i in range(5):
        idx = top5.indices[i].item()
        german_name = german_classes.get(idx, f"Klasse_{idx}")
        confidence = top5.values[i].item() * 100
        print(f"{i+1}. {german_name}: {confidence:.1f}%")
```

## Aufgabe 2: Webcam + Gradio GUI (Fortgeschritten)

### Ziel

Erstelle eine benutzerfreundliche Web-App, die Bilder von der Webcam oder hochgeladene Dateien analysiert und die erkannten Objekte anzeigt.

### Code-Snippets

#### 1. Gradio Interface erstellen

```python
import gradio as gr

def classify_image(image):
    if image is None:
        return "❌ Kein Bild ausgewählt!"
    
    # Klassifizierung (wie oben)
    # ...
    
    return results

# Einfache Web-App
interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(sources=["webcam", "upload"], type="pil"),
    outputs="markdown",
    title="� KI-Bilderkennung"
)
```

#### 2. Deutsche Namen integrieren

```python
def format_results_german(top3, german_classes):
    results = "🤖 **KI-Analyse:**\n\n"
    
    for i in range(3):
        idx = top3.indices[i].item()
        german_name = german_classes.get(idx, f"Unbekannt_{idx}")
        confidence = top3.values[i].item() * 100
        
        emoji = "🎯" if confidence > 50 else "🤔" if confidence > 20 else "🤷‍♂️"
        results += f"{emoji} **{german_name}**: {confidence:.1f}%\n"
    
    return results
```

#### 3. App starten

```python
if __name__ == "__main__":
    interface.launch(
        inbrowser=True,
        server_port=7860
    )
```

### Anwendung

1. **Datei speichern:** Speichere den Code als `webcam_ki.py`

2. **Programm starten:**

    ```bash
    python webcam_ki.py
    ```

3. **Browser öffnet sich automatisch** auf `http://localhost:7860`

4. **Ausprobieren:**
   - 📸 Webcam-Button für Live-Aufnahmen
   - 📁 Upload-Button für eigene Bilder
   - Automatische Analyse bei jedem neuen Bild

## Erweiterungsideen

### Einfach

#### Top-5 statt Top-3 anzeigen

```python
top5 = torch.topk(probabilities, 5)
```

#### Emoji-System für Kategorien

```python
def get_category_emoji(german_name):
    if any(tier in german_name.lower() for tier in ['katze', 'hund', 'pferd']):
        return "🐾"
    elif any(fahrzeug in german_name.lower() for fahrzeug in ['auto', 'bus', 'zug']):
        return "🚗"
    return "📦"
```

#### Konfidenz-Bewertung

```python
def bewerte_konfidenz(confidence):
    if confidence > 80: return "🎯 Sehr sicher"
    elif confidence > 50: return "� Ziemlich sicher" 
    elif confidence > 20: return "🤔 Unsicher"
    else: return "🤷‍♂️ Sehr unsicher"
```

### Fortgeschritten

- **Batch-Verarbeitung:** Mehrere Bilder gleichzeitig analysieren
- **Statistiken:** Welche Kategorien werden am häufigsten erkannt?
- **Filter:** Nur bestimmte Kategorien (Tiere/Fahrzeuge) anzeigen
- **Speichern:** Ergebnisse in CSV-Datei exportieren

## Debugging-Tipps

**Problem: Modell lädt nicht**

```python
# Alternative ohne Internet:
model = models.resnet18(pretrained=False)
# Oder vorher herunterladen
```

**Problem: Webcam funktioniert nicht**

- Nur Upload-Funktion nutzen: `sources=["upload"]`
- Browser-Berechtigungen prüfen

**Problem: Langsame Verarbeitung**

```python
# Kleineres Modell nutzen
model = models.mobilenet_v3_small(pretrained=True)
```

### Einfache Alternative ohne Gradio

- Auf Gradio verzichten, nur Terminal-Ausgabe nutzen
- Dateipfad eingeben und Ergebnis im Terminal anzeigen
- **Debugging:** Gradio zeigt hilfreiche Fehlermeldungen

## Experimentier-Aufgaben

**Verschiedene Modelle testen:**

```python
# Statt ResNet18
model = models.mobilenet_v3_small(pretrained=True)
model = models.efficientnet_b0(pretrained=True)
```

**Batch-Verarbeitung:**

Mehrere Bilder gleichzeitig analysieren und Ergebnisse zusammenfassen.

**Statistiken:**

Welche Kategorien kommen am häufigsten vor?
