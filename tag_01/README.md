# Tag 1: Python Grundlagen

Willkommen zu deinem ersten Python-Tag! Heute startest du deine Programmier-Reise mit den wichtigsten Python-Grundlagen. Du wirst schnell merken, dass Programmieren gar nicht so schwer ist - und ein Ansprechpartner ist immer da, wenn du Fragen hast!

## Was an diesem Tag gemacht wird

- **Variablen und Datentypen**: Wie man Daten speichert und verwendet
- **Bedingungen (if/else)**: Wie Programme Entscheidungen treffen
- **Schleifen**: Wie man Code automatisch wiederholt
- **Interaktives Zahlenraten-Spiel**: Alles zusammen in einem echten Programm

Du arbeitest heute mit einer bereits vorbereiteten `main.py` Datei, die du direkt ausführen und verstehen kannst!

## Alle nötigen Informationen

### Teil 1: Variablen und Datentypen

Variablen sind wie Behälter, in denen du Daten speichern kannst. Python kennt verschiedene Datentypen:

**String (Text)** - Für Wörter und Sätze:

```python
name = "Hans"
lieblingsfarbe = "Blau"
```

**Integer (Ganze Zahlen)** - Für Zahlen ohne Komma:

```python
alter = 17
anzahl_geschwister = 2
```

**Float (Dezimalzahlen)** - Für Zahlen mit Komma:

```python
groesse = 1.75
gewicht = 65.5
```

**Boolean (Wahr/Falsch)** - Für Ja/Nein-Werte:

```python
hat_fuehrerschein = False
ist_schueler = True
```

**Variablen verwenden:**

```python
print("Hallo", name, "- du bist", alter, "Jahre alt.")
begruessung = "Hi " + name + "!"
naechstes_jahr = alter + 1
```

### Teil 2: Bedingungen (if/else)

Bedingungen helfen deinem Programm, Entscheidungen zu treffen. Das Programm kann verschiedene Wege einschlagen, je nachdem, ob etwas wahr oder falsch ist.

**Einfache Bedingung:**

```python
if alter >= 14:
    print("Du bist alt genug für dieses Praktikum!")
else:
    print("Du bist noch zu jung.")
```

**Mehrere Bedingungen mit elif:**

```python
if alter < 14:
    print("Du bist noch sehr jung!")
elif alter < 18:
    print("Du bist ein Teenager!")
elif alter < 65:
    print("Du bist erwachsen!")
else:
    print("Du bist im Rentenalter!")
```

**Logische Operatoren (and, or):**

```python
if alter >= 16 and hat_fuehrerschein:
    print("Du darfst Auto fahren!")

if lieblingsfarbe == "rot" or lieblingsfarbe == "blau":
    print("Das sind schöne Farben!")
```

### Teil 3: Schleifen

Schleifen wiederholen Code automatisch, ohne dass du ihn mehrfach schreiben musst.

**For-Schleife mit range():**

```python
for i in range(5):
    print("Dies ist Schleife Nummer", i + 1)
```

Die `range()` Funktion erzeugt eine Folge von Zahlen:

- `range(5)` → 0, 1, 2, 3, 4 (von 0 bis 4)
- `range(1, 6)` → 1, 2, 3, 4, 5 (von 1 bis 5)

**Schleife mit Liste:**

```python
farbe = ["rot", "grün", "blau"]
for farbe in farbe:
    print("Meine Lieblingsfarbe könnte", farbe, "sein")
```

**While-Schleife:**

```python
countdown = 5
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1  # countdown = countdown - 1
print("Start!")
```

**Schleife mit Berechnung:**

```python
summe = 0
for zahl in range(1, 11):  # 1 bis 10
    summe += zahl  # summe = summe + zahl
print("Summe von 1 bis 10:", summe)
```

### Teil 4: Zahlenraten-Spiel

Das Zahlenraten-Spiel in deiner `main.py` bringt alles zusammen! Es zeigt, wie ein echtes interaktives Programm funktioniert.

**Was das Spiel macht:**

1. Computer wählt zufällige Zahl zwischen 1 und 10
2. Du rätst die Zahl
3. Computer gibt Hinweise ("zu hoch" oder "zu niedrig")
4. Spiel endet, wenn du richtig rätst

**Wichtige Konzepte im Spiel:**

```python
import random                           # Module importieren
geheime_zahl = random.randint(1, 10)    # Zufallszahl erstellen
versuche = 0                            # Zähler für Versuche
while True:                             # Endlosschleife
    tipp = int(input("Dein Tipp: "))    # Benutzereingabe
    if tipp == geheime_zahl:            # Vergleich
        break                           # Schleife beenden
```

**Nützliche Python-Befehle:**

| Befehl    | Was es macht                | Beispiel                 |
|-----------|-----------------------------|--------------------------|
| `print()` | Gibt Text aus               | `print("Hallo")`         |
| `input()` | Fragt Benutzer nach Eingabe | `name = input("Name: ")` |
| `int()`   | Wandelt in Ganzzahl um      | `alter = int("17")`      |
| `len()`   | Gibt Länge zurück           | `len("Hallo")` → 5       |
| `range()` | Erstellt Zahlenfolge        | `range(5)` → 0,1,2,3,4   |

## Aufgaben für den Tag

### Aufgabe 1: Deine persönlichen Daten

Öffne die `main.py` und ändere die Variablen `name` und `alter` auf deine eigenen Werte. Führe das Programm aus und schaue, was passiert.

### Aufgabe 2: Erweitere das Zahlenraten-Spiel

Verändere das Zahlenraten-Spiel so, dass:

- Der Zahlenbereich von 1-20 statt 1-10 geht
- Das Programm am Ende ausgibt, wie viele Versuche du gebraucht hast

### Aufgabe 3: Eigener kleiner Rechner

Erstelle ein kleines Programm (du kannst es am Ende der `main.py` hinzufügen), das:

- Nach zwei Zahlen fragt
- Diese addiert und das Ergebnis ausgibt
- Zusätzlich die Multiplikation der beiden Zahlen zeigt

## Lernziel Check

Nach diesem Tag solltest du:

- ✅ Variablen mit verschiedenen Datentypen erstellen können
- ✅ Verstehen, wie if/else-Bedingungen funktionieren  
- ✅ Einfache For- und While-Schleifen schreiben können
- ✅ Ein interaktives Programm verstehen und ausführen können

## Tipps

- **Fehler sind völlig normal!** Jeder Programmierer macht täglich Fehler - das gehört dazu
- **Experimentiere viel**: Ändere Werte in der `main.py` und schaue, was passiert
- **Frag immer nach**: Ein Ansprechpartner ist da, wenn du etwas nicht verstehst
- **Klein anfangen**: Große Programme bestehen aus vielen kleinen, einfachen Teilen
- **Nutze Kommentare**: Schreibe `# Kommentar` für deine eigenen Notizen im Code

## Du schaffst das

Herzlichen Glückwunsch - du hast deine ersten Schritte in die Python-Programmierung gemacht! Das waren schon alle wichtigen Grundlagen. Wenn du Fragen hast oder etwas nicht funktioniert, frag einfach nach.

Morgen geht es weiter mit einem spannenden Text-Adventure und du lernst Git kennen. Bis dahin: Experimentiere gerne mit dem Code und hab Spaß dabei!
