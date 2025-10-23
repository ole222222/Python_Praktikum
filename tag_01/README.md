# Python-Starterpaket für Ole 👋

Willkommen zu deinem ersten Python-Projekt in VS Code! Hier lernst du die Grundlagen der Python-Programmierung mit praktischen Beispielen.

## Was du in diesem Tag lernst

- **Variablen und Datentypen**: Wie man Daten speichert und verwendet
- **Bedingungen**: Wie Programme Entscheidungen treffen
- **Schleifen**: Wie man Code wiederholt
- **Interaktive Programme**: Ein kleines Zahlenraten-Spiel

## Teil 1: Variablen und Datentypen

Variablen sind wie Behälter, in denen du Daten speichern kannst.

### Beispiele aus der main.py

```python
name = "Hans"       # String (Text)
alter = 17          # Integer (Ganze Zahl)
print("Hallo", name, "- du bist", alter, "Jahre alt.")
```

### Weitere Beispiele zum Ausprobieren

```python
# Verschiedene Datentypen
lieblingsfarbe = "Blau"    # String (Text)
groesse = 1.75             # Float (Dezimalzahl)
hat_fuehrerschein = False  # Boolean (True/False)

# Variablen kombinieren
begruessung = "Hi " + name + "!"
naechstes_jahr = alter + 1

print(begruessung)
print("Nächstes Jahr bist du", naechstes_jahr)
```

## Teil 2: Bedingungen (if/else)

Bedingungen helfen deinem Programm, Entscheidungen zu treffen.

### Beispiel aus der main.py

```python
if alter >= 14:
    print("Du bist alt genug für dieses Praktikum!")
else:
    print("Du bist noch zu jung.")
```

### Erweiterte Bedingungen

```python
# Mehrere Bedingungen
if alter < 14:
    print("Du bist noch sehr jung!")
elif alter < 18:
    print("Du bist ein Teenager!")
elif alter < 65:
    print("Du bist erwachsen!")
else:
    print("Du bist im Rentenalter!")

# Logische Operatoren
if alter >= 16 and hat_fuehrerschein:
    print("Du darfst Auto fahren!")
```

## Teil 3: Schleifen

Schleifen wiederholen Code automatisch.

### For-Schleife aus der main.py

```python
for i in range(5):
    print("Dies ist Schleife Nummer", i + 1)
```

### range() Funktion

Die `range()` Funktion erzeugt eine Folge von Zahlen.
Sie zählt von 0 bis zu einer angegebenen Zahl (exklusiv).

```python
for zahl in range(1, 6):  # Zählt von 1 bis 5
    print(zahl)
```

### Verschiedene Schleifenarten

```python
# For-Schleife mit Liste
farben = ["rot", "grün", "blau"]
for farbe in farben:
    print("Meine Lieblingsfarbe könnte", farbe, "sein")

# While-Schleife
countdown = 5
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1
print("Start!")

# Schleife mit Berechnung
summe = 0
for zahl in range(1, 11):  # 1 bis 10
    summe += zahl
print("Summe von 1 bis 10:", summe)
```

## Teil 4: Zahlenraten-Spiel

Ein interaktives Spiel, das alles zusammenführt!

### Was das Spiel macht

1. Computer wählt zufällige Zahl zwischen 1 und 10
2. Du rätst die Zahl
3. Computer gibt Hinweise ("zu hoch" oder "zu niedrig")
4. Spiel endet, wenn du richtig rätst

### Wichtige Konzepte im Spiel

```python
import random                           # Module importieren
geheime_zahl = random.randint(1, 10)    # Zufallszahl
versuche = 0                            # Zähler
while True:                             # Endlosschleife
    tipp = int(input("Dein Tipp: "))    # Benutzereingabe
    if tipp == geheime_zahl:            # Vergleich
        break                           # Schleife beenden
```

## Experimentiere selbst

### Einfache Änderungen

- Ändere den Namen und das Alter in den Variablen
- Vergrößere den Zahlenbereich im Spiel (z.B. 1-100)
- Füge mehr Farben zur Farbenliste hinzu

### Fortgeschrittene Ideen

```python
# Rechner
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))
ergebnis = zahl1 + zahl2
print("Ergebnis:", ergebnis)

# Passwort-Checker
passwort = input("Gib ein Passwort ein: ")
if len(passwort) >= 8:
    print("Starkes Passwort!")
else:
    print("Passwort zu kurz!")
```

## So führst du den Code aus

1. Öffne `main.py` in VS Code
2. Drücke `F5` oder klicke auf "Run Python File"
3. Folge den Anweisungen im Terminal
4. Experimentiere mit dem Code!

## Nützliche Python-Befehle

| Befehl    | Was es macht                | Beispiel                 |
|-----------|-----------------------------|--------------------------|
| `print()` | Gibt Text aus               | `print("Hallo")`         |
| `input()` | Fragt Benutzer nach Eingabe | `name = input("Name: ")` |
| `int()`   | Wandelt in Ganzzahl um      | `alter = int("17")`      |
| `len()`   | Gibt Länge zurück           | `len("Hallo")` → 5       |
| `range()` | Erstellt Zahlenfolge        | `range(5)` → 0,1,2,3,4   |

## Lernziele Check

Nach diesem Tag solltest du:

- ✅ Variablen erstellen und verwenden können
- ✅ Verstehen, wie if/else funktioniert
- ✅ Einfache Schleifen schreiben können
- ✅ Ein interaktives Programm verstehen

## Tipps

- **Fehler sind normal!** Jeder Programmierer macht Fehler
- **Experimentiere viel**: Ändere Werte und schaue, was passiert
- **Nutze Comments**: Schreibe `# Kommentar` für Notizen
- **Klein anfangen**: Große Programme bestehen aus vielen kleinen Teilen

## Hilfe und nächste Schritte

- Frag jederzeit, wenn du etwas nicht verstehst!
- Schau dir die anderen Tags an, wenn du bereit bist
- Denke dir eigene kleine Programme aus

Viel Spaß beim Programmieren!
