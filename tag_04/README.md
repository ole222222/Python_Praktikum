# Tag 4: Erweiterte KI-Projekte & Computer Vision

Willkommen zu Tag 4! Heute vertiefen wir das KI-Wissen und entwickeln praktische Computer Vision Anwendungen. Der Fokus liegt auf Objekterkennung, Gesichtserkennung und ethischen Aspekten der KI-Entwicklung.

## Was du heute lernst

- **YOLO Objekterkennung**: Mehrere Objekte gleichzeitig erkennen und markieren
- **Gesichtserkennung**: Face Detection und ethische Überlegungen
- **Computer Vision**: Erweiterte Bildverarbeitung mit OpenCV
- **Projektstrukturierung**: Komplexere Python-Programme organisieren
- **KI-Ethik**: Verantwortlicher Umgang mit KI-Technologie

## Teil 1: Projekt-Setup und Umgebung

### Benötigte Bibliotheken installieren

```bash
pip install ultralytics opencv-python pillow numpy matplotlib
```

### Was sind diese Bibliotheken?

- **ultralytics**: Moderne YOLO-Implementierung für Objekterkennung (inkl. YOLO11)
- **opencv-python**: Bildverarbeitung und Computer Vision
- **pillow**: Bildbearbeitung und -formate
- **numpy**: Numerische Berechnungen für Bildverarbeitung
- **matplotlib**: Visualisierung und Bildanzeige

## Teil 2: YOLO Objekterkennung verstehen

### Was ist YOLO?

**YOLO** = "You Only Look Once"

- Erkennt **mehrere Objekte** gleichzeitig in einem Bild
- Zeichnet **Bounding Boxes** um erkannte Objekte
- Gibt **Confidence Scores** (Wahrscheinlichkeiten) aus
- Sehr schnell - geeignet für Real-Time Anwendungen

### Grundkonzepte

```python
# Basiskonzept: Ein Modell, viele Objekte
model = YOLO('yolo11n.pt')  # YOLO11 nano - neueste Version!
results = model('bild.jpg')

# Was kommt zurück?
for result in results:
    boxes = result.boxes          # Bounding Boxes
    classes = result.names        # Erkannte Klassen
    confidence = boxes.conf       # Wahrscheinlichkeiten
```

### Praktische Anwendung

**Siehe detailliertes Tutorial**: `YOLO_Objekterkennung.md`

## Teil 3: Gesichtserkennung und Ethik

### Computer Vision vs. Gesichtserkennung

**Computer Vision** (harmlos):

- Objekte zählen: "5 Äpfel im Bild"
- Tiere erkennen: "Das ist ein Hund"
- Qualitätskontrolle: "Produkt ist defekt"

**Gesichtserkennung** (ethisch kritisch):

- Personen identifizieren
- Emotionen analysieren
- Überwachung ermöglichen

### Warum ist das problematisch?

```python
# Technisch einfach, ethisch kompliziert
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Das Modell kann Gesichter erkennen...
# Aber SOLLTE es das in dieser Anwendung?
```

### Ethische Leitfragen

- **Zweck**: Warum erkenne ich Gesichter?
- **Einverständnis**: Haben die Personen zugestimmt?
- **Speicherung**: Werden biometrische Daten gespeichert?
- **Sicherheit**: Wie schütze ich die Daten?

## Teil 4: Praktische Übungen

### Übung 1: Objekt-Zähler (Einfach)

Erstelle ein Programm, das Objekte in einem Bild zählt:

```python
def count_objects(image_path, target_class="person"):
    """
    Zählt bestimmte Objekte in einem Bild
    
    Args:
        image_path: Pfad zum Bild
        target_class: Zu zählende Objektklasse
    
    Returns:
        Anzahl der gefundenen Objekte
    """
    # Dein Code hier...
    pass
```

### Übung 2: Sicherheits-Kamera Simulator (Mittel)

Simuliere eine Überwachungskamera, die nur Fahrzeuge erkennt:

```python
def security_monitor(image_path):
    """
    Überwacht Bild nach Fahrzeugen
    Zeigt Warnung bei unbekannten Objekten
    """
    allowed_objects = ["car", "truck", "bus", "motorcycle"]
    # Implementation...
```

### Übung 3: YOLO Version Battle (Fortgeschritten)

Führe einen direkten Vergleich zwischen YOLO11 und YOLO8 durch:

```python
def yolo_version_battle(image_path):
    """
    YOLO11 vs YOLO8 Showdown!
    
    Vergleiche:
    - Anzahl erkannter Objekte
    - Confidence Scores
    - Verarbeitungszeit
    - Speicherverbrauch
    """
    import time
    
    # Lade beide Modelle
    model_11 = YOLO('yolo11n.pt')
    model_8 = YOLO('yolov8n.pt')
    
    # Performance-Test
    # Deine Implementierung hier...
    
    # Ergebnis: Welches Modell ist besser?
    pass
```

### Model-Größen vergleichen

| Modell  | Größe  | Geschwindigkeit | Genauigkeit | Verwendung               |
| ------- | ------ | --------------- | ----------- | ------------------------ |
| yolo11n | Klein  | Sehr schnell    | Gut         | Prototyping, mobile Apps |
| yolo11s | Mittel | Schnell         | Besser      | Ausgewogene Anwendungen  |
| yolo11m | Groß   | Langsamer       | Sehr gut    | Hohe Genauigkeit wichtig |

### YOLO11 vs YOLO8 Vergleich (Experimentier-Aufgabe)

Teste beide Versionen und vergleiche sie:

```python
def compare_yolo_versions(image_path):
    """
    Vergleicht YOLO11 mit YOLO8 Performance
    
    Experimentiere mit:
    - Geschwindigkeit
    - Genauigkeit
    - Erkannte Objekte
    """
    # YOLO11 (neueste Version)
    model_v11 = YOLO('yolo11n.pt')
    
    # YOLO8 (ältere Version)
    model_v8 = YOLO('yolov8n.pt')
    
    # Deine Vergleiche hier...
    pass
```

## Lernziele Check

Nach diesem Tag solltest du:

- ✅ YOLO für Objekterkennung verwenden können
- ✅ Bounding Boxes und Confidence Scores verstehen
- ✅ Ethische Aspekte von Gesichtserkennung kennen
- ✅ OpenCV für Bildverarbeitung nutzen können
- ✅ Computer Vision Projekte strukturieren können
- ✅ Git für KI-Entwicklung einsetzen können

## Teil 5: Git-Workflow für heute

### Branch für Experimentierung

```bash
# Neuen Branch für YOLO-Experimente erstellen
git checkout -b feature-yolo11-vs-yolo8

# Regelmäßig speichern
git add .
git commit -m "Add YOLO11 object detection implementation"

# Ergebnisse dokumentieren
git commit -m "Add YOLO11 vs YOLO8 performance comparison"
```

## Teil 6: Herausforderungen

### Einfach

- Erkenne alle Fahrzeuge in einem Verkehrsbild mit YOLO11
- Zähle die Anzahl der Personen in einem Gruppenfoto (ethisch!)
- Erstelle eine Liste aller erkannten Objektklassen

### Mittel

- **YOLO Battle**: Vergleiche YOLO11 vs YOLO8 Performance auf 5 verschiedenen Bildern
- Entwickle einen "Smart Parking" Detektor mit YOLO11
- Baue ein System zur Qualitätskontrolle für Produkte

### Schwer

- Kombiniere YOLO11 Objekterkennung mit ethischer Gesichtserkennung
- Erstelle ein Real-Time Dashboard für Objekterkennung
- Entwickle ein Performance-Benchmark-Tool für verschiedene YOLO-Versionen

## Tipps für erfolgreiche KI-Projekte

### Entwicklung

- **Klein anfangen**: Erst einfache Beispiele, dann erweitern
- **Testen mit verschiedenen Bildern**: Nicht nur auf einem Bild arbeiten
- **Error Handling**: KI-Modelle können unerwartete Eingaben bekommen
- **Performance beobachten**: Messe Geschwindigkeit und Speicherverbrauch

### Ethik

- **Zweck definieren**: Warum nutze ich diese Technologie?
- **Grenzen beachten**: Nicht alles was möglich ist, ist auch richtig
- **Transparenz**: Dokumentiere, was dein System macht
- **Datenschutz**: Keine persönlichen Daten ohne Einverständnis
