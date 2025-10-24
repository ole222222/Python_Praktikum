# Tag 4: YOLO Objekterkennung - Dinge im Bild finden und markieren

Herzlich willkommen zu Tag 4! Heute wirst du lernen, wie Computer "sehen" können und mehrere Objekte gleichzeitig in Bildern erkennen. Du wirst YOLO (You Only Look Once) kennenlernen - eine faszinierende Technologie, die in selbstfahrenden Autos, Sicherheitskameras und vielen anderen Anwendungen verwendet wird.

Falls du Fragen hast oder etwas nicht verstehst - zögere nicht zu fragen! Ein Ansprechpartner ist immer da, um dir zu helfen.

## Was an diesem Tag gemacht wird

- **YOLO Objekterkennung**: Lerne, wie Computer mehrere Objekte gleichzeitig in einem Bild erkennen
- **Bounding Boxes**: Verstehe, wie erkannte Objekte mit Rechtecken markiert werden
- **Ultralytics YOLO**: Nutze eine der modernsten Objekterkennungs-Bibliotheken
- **Praktische Anwendung**: Erkenne Autos, Personen, Tiere und andere Objekte in echten Bildern
- **Programmstruktur**: Organisiere deinen Code sauberer mit Funktionen

## Alle nötigen Informationen

### Was ist YOLO?

**YOLO** steht für "You Only Look Once" (Du schaust nur einmal hin). Es ist eine sehr clevere Art, wie Computer Bilder verstehen können:

- **Mehrere Objekte gleichzeitig**: YOLO kann in einem Bild viele verschiedene Dinge auf einmal erkennen
- **Bounding Boxes**: Um jedes erkannte Objekt wird ein Rechteck gezeichnet
- **Confidence Score**: Das System sagt uns, wie sicher es sich bei der Erkennung ist (z.B. 85% sicher, dass es ein Auto ist)
- **Sehr schnell**: YOLO ist so schnell, dass es in Echtzeit funktioniert

### Bibliotheken installieren

Heute brauchst du neue Python-Pakete. Öffne PowerShell und installiere sie:

```powershell
pip install ultralytics opencv-python pillow matplotlib
```

**Was diese Pakete machen:**

- **ultralytics**: Die moderne YOLO-Bibliothek für Objekterkennung
- **opencv-python**: Für Bildverarbeitung und das Anzeigen von Bildern
- **pillow**: Zum Öffnen und Bearbeiten verschiedener Bildformate
- **matplotlib**: Zum schönen Anzeigen der Ergebnisse

### Wie YOLO funktioniert (vereinfacht)

```python
from ultralytics import YOLO

# 1. Modell laden (das "Gehirn" für Objekterkennung)
model = YOLO('yolo11n.pt')  # 'n' steht für "nano" = klein und schnell

# 2. Bild analysieren
results = model('mein_bild.jpg')

# 3. Ergebnisse anschauen
for result in results:
    boxes = result.boxes        # Die Rechtecke um die Objekte
    names = result.names        # Was wurde erkannt (Auto, Person, etc.)
    confidence = boxes.conf     # Wie sicher ist das System?
```

### Bounding Boxes verstehen

Eine **Bounding Box** ist ein Rechteck um ein erkanntes Objekt:

```python
# Beispiel einer Bounding Box
# x1, y1 = linke obere Ecke
# x2, y2 = rechte untere Ecke
# Das Rechteck umschließt das gefundene Objekt

for box in boxes:
    x1, y1, x2, y2 = box.xyxy[0]  # Koordinaten der Box
    confidence = box.conf[0]       # Wie sicher? (0.0 bis 1.0)
    class_id = box.cls[0]          # Was wurde erkannt?
    
    print(f"Gefunden: {names[int(class_id)]} mit {confidence:.2f} Sicherheit")
```

### YOLO-Modellgrößen

Es gibt verschiedene YOLO-Modelle - je größer, desto genauer, aber auch langsamer:

| Modell     | Geschwindigkeit | Genauigkeit | Gut für                    |
|------------|-----------------|-------------|----------------------------|
| `yolo11n.pt` | Sehr schnell    | Gut         | Erste Experimente         |
| `yolo11s.pt` | Schnell         | Besser      | Ausgewogene Projekte      |
| `yolo11m.pt` | Langsamer       | Sehr gut    | Wenn Genauigkeit wichtig ist |

### Objekte, die YOLO erkennen kann

YOLO kann 80 verschiedene Objekttypen erkennen, zum Beispiel:

- **Personen**: person
- **Fahrzeuge**: car, truck, bus, motorcycle, bicycle
- **Tiere**: dog, cat, horse, bird, cow
- **Objekte**: bottle, chair, laptop, book, apple

Die vollständige Liste findest du, wenn du `model.names` ausgibst.

## Aufgaben für den Tag

### Aufgabe 1: Mein erstes YOLO-Programm (Einfach)

Erstelle eine neue Python-Datei `objekt_erkennner.py` und schreibe ein Programm, das Objekte in einem Bild erkennt und anzeigt:

```python
# Importiere die YOLO-Bibliothek
from ultralytics import YOLO

# Lade das YOLO-Modell
model = YOLO('yolo11n.pt')  # Das wird automatisch heruntergeladen

# Analysiere ein Bild aus dem yolo_bilder Ordner
results = model('yolo_bilder/image.jpg')

# Zeige das Ergebnis an
results[0].show()  # Öffnet ein Fenster mit dem Bild und den erkannten Objekten
```

**Experimentiere mit verschiedenen Bildern:**

- Teste `image.jpg`, `image2.jpg`, `image3.jpg` und `obst.jpg`
- Was erkennt YOLO in jedem Bild?
- Welche Confidence Scores siehst du?

### Aufgabe 2: Objekt-Zähler erstellen (Mittel)

Schreibe ein Programm, das bestimmte Objekte in einem Bild zählt:

```python
def zaehle_objekte(bild_pfad, objekt_typ="person"):
    """
    Zählt bestimmte Objekte in einem Bild
    
    Args:
        bild_pfad: Pfad zum Bild (z.B. 'yolo_bilder/image.jpg')
        objekt_typ: Was soll gezählt werden? (z.B. "person", "car", "dog")
    
    Returns:
        Anzahl der gefundenen Objekte
    """
    model = YOLO('yolo11n.pt')
    results = model(bild_pfad)
    
    # Hier musst du den Code zum Zählen schreiben...
    # Tipp: Schaue dir result.boxes.cls und result.names an
    
    return anzahl

# Teste deine Funktion
anzahl_personen = zaehle_objekte('yolo_bilder/image.jpg', 'person')
print(f"Ich habe {anzahl_personen} Personen gefunden!")
```

**Erweitere das Programm:**

- Zähle verschiedene Objekttypen in verschiedenen Bildern
- Zeige eine Liste aller erkannten Objekttypen an
- Finde heraus, welches Bild die meisten Objekte hat

### Aufgabe 3: Foto-Analyse-Tool (Fortgeschritten)

Erstelle ein umfassendes Tool, das ein Bild vollständig analysiert:

```python
def analysiere_foto(bild_pfad):
    """
    Analysiert ein Foto vollständig und gibt einen Bericht aus
    """
    model = YOLO('yolo11n.pt')
    results = model(bild_pfad)
    
    print(f"=== FOTO-ANALYSE: {bild_pfad} ===")
    print()
    
    # Teil 1: Alle erkannten Objekte auflisten
    print("Erkannte Objekte:")
    # Dein Code hier...
    
    # Teil 2: Objekte nach Typ gruppieren und zählen
    print("\nAnzahl nach Objekttyp:")
    # Dein Code hier...
    
    # Teil 3: Confidence Scores analysieren
    print("\nSicherheits-Statistiken:")
    print(f"Höchste Sicherheit: {max_confidence:.2f}")
    print(f"Niedrigste Sicherheit: {min_confidence:.2f}")
    print(f"Durchschnittliche Sicherheit: {avg_confidence:.2f}")
    
    # Zeige das Bild mit Markierungen
    results[0].show()

# Teste mit allen Bildern
bilder = ['image.jpg', 'image2.jpg', 'image3.jpg', 'obst.jpg']
for bild in bilder:
    analysiere_foto(f'yolo_bilder/{bild}')
    print("\n" + "="*50 + "\n")
```

## Lernziel Check

Nach diesem Tag solltest du:

- ✅ YOLO für Objekterkennung verwenden können
- ✅ Verschiedene Objekte in Bildern erkennen und zählen
- ✅ Verstehen, was Bounding Boxes und Confidence Scores sind
- ✅ Eigene Python-Dateien für YOLO-Projekte erstellen können
- ✅ Mit verschiedenen YOLO-Modellgrößen experimentieren
- ✅ Die Ergebnisse von Objekterkennung interpretieren können

## Tipps

### Wenn das Programm nicht funktioniert

- **Modell lädt nicht**: Beim ersten Mal dauert es länger, da YOLO heruntergeladen wird
- **Bild wird nicht gefunden**: Überprüfe den Pfad zu deinen Bildern (z.B. `yolo_bilder/image.jpg`)
- **Keine Objekte erkannt**: Nicht alle Bilder enthalten erkennbare Objekte - das ist normal!
- **Programm ist langsam**: Das nano-Modell (`yolo11n.pt`) ist am schnellsten

### Häufige Fehler vermeiden

```python
# RICHTIG: Verwende den korrekten Pfad
results = model('yolo_bilder/image.jpg')

# FALSCH: Vergessener Ordnername
results = model('image.jpg')  # Datei nicht gefunden!

# RICHTIG: Überprüfe, ob Boxen vorhanden sind
if len(results[0].boxes) > 0:
    print("Objekte gefunden!")
else:
    print("Keine Objekte erkannt.")
```

### Experimentier-Ideen

- Teste verschiedene Bilder und schaue, was YOLO erkennt
- Vergleiche die nano-, small- und medium-Modelle
- Erstelle eine Statistik über alle deine Testbilder
- Finde heraus, welche Objekttypen am häufigsten erkannt werden

### Debugging-Hilfen

```python
# Zeige alle verfügbaren Objektklassen
model = YOLO('yolo11n.pt')
print("YOLO kann diese Objekte erkennen:")
for i, name in enumerate(model.names.values()):
    print(f"{i}: {name}")

# Zeige Details über erkannte Objekte
results = model('yolo_bilder/image.jpg')
for i, box in enumerate(results[0].boxes):
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    class_name = model.names[class_id]
    print(f"Objekt {i+1}: {class_name} ({confidence:.2f} sicher)")
```

## Du hast Tag 4 geschafft!

Gratulation! Du hast heute gelernt, wie Computer "sehen" können. YOLO-Objekterkennung wird in vielen echten Anwendungen verwendet - von selbstfahrenden Autos bis zu Qualitätskontrolle in Fabriken. 

Du hast jetzt die Grundlagen, um:

- Objekte in Bildern automatisch zu erkennen
- Programme zu schreiben, die Bilder verstehen können
- Die Basis für komplexere Computer Vision Projekte

Morgen in Tag 5 werden wir diese Fähigkeiten nutzen, um ein intelligentes Text-Adventure zu erstellen, das mit KI-Unterstützung noch spannender wird!

Denke daran: Wenn du Fragen hast oder etwas nicht verstehst, ist immer jemand da, um dir zu helfen. Das Experimentieren und Ausprobieren ist ein wichtiger Teil des Lernens!
