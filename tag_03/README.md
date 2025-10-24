# Tag 3: Deep Learning mit PyTorch - Bilderkennung

Willkommen zu Tag 3 deines Python-Praktikums! Heute tauchen wir in die spannende Welt des Deep Learning ein. Du wirst lernen, wie Computer "sehen" können und eigene KI-Anwendungen für Bilderkennung entwickeln. Das klingt kompliziert, aber du wirst staunen, wie einfach es mit den richtigen Tools sein kann!

## Was an diesem Tag gemacht wird

Heute lernst du die praktische Anwendung von Deep Learning kennen und entwickelst eigene Anwendungen für Bilderkennung. Du wirst:

- Ein vortrainiertes neuronales Netzwerk verwenden
- Deutsche Klassifizierung von Bildern durchführen
- Eine benutzerfreundliche Web-Oberfläche erstellen
- Echte Bilder von der Webcam oder aus Dateien analysieren

**Wichtig:** Du musst nicht verstehen, wie Deep Learning im Detail funktioniert - wir zeigen dir einfach, wie du es nutzen kannst!

## Alle nötigen Informationen

### Was ist Deep Learning?

Deep Learning ist eine Methode, mit der Computer lernen können, Muster in Daten zu erkennen - ähnlich wie unser Gehirn. Für Bilderkennung bedeutet das: Der Computer kann lernen, Objekte auf Fotos zu identifizieren.

**Du musst die Theorie nicht verstehen** - wir nutzen einfach fertige Modelle, die bereits trainiert wurden!

### PyTorch Installation

PyTorch ist eine beliebte Bibliothek für Deep Learning. Wir installieren alle benötigten Pakete:

```powershell
pip install torch torchvision pillow matplotlib requests gradio
```

**Was installiert wird:**

- `torch` - PyTorch Deep Learning Bibliothek
- `torchvision` - Modelle und Tools für Bildverarbeitung  
- `pillow` - Bildverarbeitung
- `matplotlib` - Diagramme erstellen
- `requests` - Dateien aus dem Internet laden
- `gradio` - Web-Oberflächen erstellen

### Vortrainierte Modelle

Ein "vortrainiertes Modell" ist wie ein sehr erfahrener Experte für Bilderkennung. Diese Modelle wurden bereits mit Millionen von Bildern trainiert und können 1000 verschiedene Objekttypen erkennen.

**ResNet18** ist so ein Modell - klein, schnell und trotzdem sehr genau.

### Deutsche Klassennamen

In diesem Praktikum nutzen wir deutsche Übersetzungen für die erkannten Objekte. Die Datei `imagenet_german/imagenet_deutsch_vollstaendig.json` enthält alle Übersetzungen.

### Grundlegende Code-Struktur

```python
# 1. Bibliotheken laden
import torch
from torchvision import models, transforms
from PIL import Image

# 2. Modell laden
model = models.resnet18(pretrained=True)
model.eval()

# 3. Bild vorbereiten
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

# 4. Bild klassifizieren
def classify_image(image_path):
    img = Image.open(image_path).convert('RGB')
    input_tensor = transform(img).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    return probabilities
```

## Aufgaben für den Tag

### Aufgabe 1: Erste Bilderkennung mit deutscher Ausgabe

**Ziel:** Erstelle ein Programm, das Bilder aus dem `bilder_test/` Ordner analysiert und die erkannten Objekte auf Deutsch ausgibt.

**Was du machst:**

1. Ein vortrainiertes Modell laden
2. Deutsche Klassennamen aus der JSON-Datei lesen  
3. Ein Testbild analysieren und die Top 3 Ergebnisse anzeigen

**Hilfreiche Code-Snippets:**

Modell laden:

```python
import torch
from torchvision import models, transforms

# Vortrainiertes ResNet18 Modell laden
model = models.resnet18(pretrained=True)
model.eval()  # Auf Auswertungs-Modus setzen
```

Deutsche Klassen laden:

```python
import json

def load_german_classes():
    with open('imagenet_german/imagenet_deutsch_vollstaendig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Dictionary erstellen: Index -> deutscher Name
    translations = {}
    for item in data['uebersetzungen']:
        translations[item['index']] = item['deutsch']
    
    return translations
```

Bild vorbereiten:

```python
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
```

Klassifizierung durchführen:

```python
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
```

**Erfolgskriterium:** Dein Programm zeigt für ein Testbild die Top 3 erkannten Objekte mit deutschen Namen und Prozent-Werten an.

### Aufgabe 2: Interaktive Bilderkennung mit Web-Oberfläche

**Ziel:** Erstelle eine benutzerfreundliche Web-App, die Bilder von der Webcam oder hochgeladene Dateien analysiert.

**Was du machst:**

1. Eine Web-Oberfläche mit Gradio erstellen
2. Webcam-Unterstützung einbauen
3. Upload-Funktionalität hinzufügen
4. Schöne Ausgabe der Ergebnisse

**Hilfreiche Code-Snippets:**

Gradio Interface:

```python
import gradio as gr

def analyze_image_for_web(image):
    if image is None:
        return "Kein Bild ausgewählt!"
    
    # Hier deine Klassifizierungs-Funktion nutzen
    # ...
    
    # Schöne Markdown-Ausgabe erstellen
    result = "## KI-Analyse Ergebnis\n\n"
    result += "**Top 3 Erkennungen:**\n\n"
    
    # Hier die Top 3 hinzufügen
    # ...
    
    return result

# Web-Interface erstellen
interface = gr.Interface(
    fn=analyze_image_for_web,
    inputs=gr.Image(sources=["webcam", "upload"], type="pil"),
    outputs="markdown",
    title="KI-Bilderkennung mit deutschen Namen"
)
```

Interface starten:

```python
if __name__ == "__main__":
    interface.launch(inbrowser=True, server_port=7860)
```

**Erfolgskriterium:** Deine Web-App öffnet sich im Browser, du kannst Bilder hochladen oder mit der Webcam aufnehmen und bekommst deutsche Klassifizierungen angezeigt.

### Aufgabe 3: Batch-Verarbeitung aller Testbilder

**Ziel:** Analysiere alle Bilder im `bilder_test/` Ordner automatisch und erstelle eine Übersicht der Ergebnisse.

**Was du machst:**

1. Alle Bilddateien im Ordner finden
2. Jedes Bild analysieren  
3. Ergebnisse in einer übersichtlichen Liste ausgeben
4. Optional: Ergebnisse in eine Textdatei speichern

**Hilfreiche Code-Snippets:**

Alle Bilddateien finden:

```python
import os
from pathlib import Path

def find_image_files(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    image_files = []
    
    for file_path in Path(folder_path).iterdir():
        if file_path.suffix.lower() in image_extensions:
            image_files.append(str(file_path))
    
    return image_files
```

Batch-Verarbeitung:

```python
def analyze_all_images(folder_path, model, german_classes):
    image_files = find_image_files(folder_path)
    
    print(f"Analysiere {len(image_files)} Bilder...")
    print("=" * 50)
    
    for image_path in image_files:
        classify_image(image_path, model, german_classes)
        print("-" * 30)
```

Ergebnisse speichern:

```python
def save_results_to_file(results, output_file="analysis_results.txt"):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Bilderkennung Ergebnisse\n")
        f.write("=" * 30 + "\n\n")
        
        for result in results:
            f.write(result + "\n")
    
    print(f"Ergebnisse gespeichert in: {output_file}")
```

**Erfolgskriterium:** Alle Testbilder werden automatisch analysiert und du bekommst eine übersichtliche Liste aller Erkennungen.

## Lernziel Check

Nach diesem Tag kannst du:

- ✅ Ein vortrainiertes Deep Learning Modell laden und verwenden
- ✅ Deutsche Klassifizierungen von Bildern durchführen  
- ✅ Eine Web-Oberfläche mit Gradio erstellen
- ✅ Bilder von der Webcam und Uploads verarbeiten
- ✅ Mehrere Bilder automatisch analysieren (Batch-Verarbeitung)
- ✅ Deep Learning praktisch anwenden, ohne die Theorie zu verstehen

## Tipps

**Bei Problemen mit der Installation:**

- Überprüfe deine Python-Version: `python --version` (sollte 3.11 sein)
- Nutze `pip list` um zu sehen, welche Pakete installiert sind
- Bei Fehlern: Einzelne Pakete nachinstallieren

**Webcam-Probleme:**

- Browser-Berechtigungen für Kamera prüfen
- Alternativ nur Upload-Funktion nutzen
- Andere Browser ausprobieren

**Modell lädt langsam:**

- Das erste Mal dauert es länger (Download)
- Danach wird es im Cache gespeichert
- Alternative: Kleinere Modelle wie MobileNet verwenden

**Debugging-Hilfe:**

- `print()` Statements für Zwischenergebnisse nutzen
- Einzelne Code-Teile zuerst separat testen
- Bei Fehlern: Genaue Fehlermeldung lesen

**Wichtig:** Du hast immer einen Ansprechpartner zur Verfügung! Zögere nicht, Fragen zu stellen oder um Hilfe zu bitten. Niemand erwartet, dass du alles sofort verstehst.

## Du hast Tag 3 geschafft!

Herzlichen Glückwunsch! Du hast gerade deine ersten Deep Learning Anwendungen erstellt und kannst jetzt Computer "sehen" lassen. Das ist ein riesiger Schritt in der Welt der Künstlichen Intelligenz!

**Dein nächster Schritt:** Morgen geht es mit Tag 4 weiter, wo du lernst, nicht nur Objekte zu erkennen, sondern auch ihre Position im Bild zu finden. Das wird noch beeindruckender!

**Vergiss nicht:** Experimentiere gerne mit den Codes weiter, probiere andere Bilder aus und hab Spaß mit deinen neuen KI-Fähigkeiten!
