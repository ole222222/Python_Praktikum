# Tag 2: Text-Adventure & Git/GitHub Grundlagen

Willkommen zu Tag 2 deines Python-Praktikums! Heute machst du einen großen Schritt in deiner Programmier-Reise. Du wirst dein erstes Text-Adventure erstellen und die wichtigen Grundlagen von Git und GitHub kennenlernen. Keine Sorge - ein Ansprechpartner ist immer da, wenn du Fragen hast!

## Was an diesem Tag gemacht wird

- **Text-Adventure Spiel**: Ein interaktives Abenteuer mit Funktionen programmieren
- **Python-Wiederholung**: Festigung von Variablen, Bedingungen und Input/Output
- **Funktionen**: Zum ersten Mal eigene Funktionen schreiben und verstehen
- **Git Grundlagen**: Versionskontrolle verstehen und praktisch nutzen
- **GitHub Workflow**: Code sichern, teilen und zusammenarbeiten
- **Wichtige Git-Befehle**: commit, push, pull, fetch, fork, branch verstehen

## Teil 1: Text-Adventure (Aufwärmung)

Lass uns mit einem einfachen Text-Adventure-Spiel starten, um das Gelernte aus Tag 1 zu wiederholen!

### Das aktuelle Spiel verstehen

Schau dir die `main.py` an:

```python
def start_game():
    print("Willkommen zu deinem Abenteuer!")
    print("Du stehst vor zwei Türen: links und rechts.")
    choice = input("Welche Tür wählst du? (links/rechts): ").strip().lower()

    if choice == "links":
        print("Du findest einen Schatz! 🎉")
    elif choice == "rechts":
        print("Ein Monster erscheint! 🐉")
    else:
        print("Du hast dich verirrt...")
```

### Neu: Was sind Funktionen?

Das Spiel nutzt etwas Neues: **Funktionen**! Das war in Tag 1 noch nicht dran.

```python
def start_game():  # ← Das ist eine Funktions-Definition
    print("Willkommen zu deinem Abenteuer!")
    # ... mehr Code ...

start_game()  # ← Das ist ein Funktions-Aufruf
```

**Was sind Funktionen?**

- Wie ein Rezept: Einmal schreiben, oft verwenden
- Machen Code übersichtlicher und wieder verwendbar
- `def` = "definiere eine neue Funktion"

### Wiederholung der Python-Konzepte aus Tag 1

Das Spiel nutzt auch alles aus Tag 1:

- **Variablen**: `choice = input(...)`
- **Bedingungen**: `if/elif/else`
- **String-Methoden**: `.strip().lower()`
- **Input/Output**: `print()` und `input()`

### Spiel starten

```bash
python main.py
```

### Kleine Verbesserungsideen

Experimentiere mit kleinen Änderungen:

```python
# Idee 1: Mehr Auswahlmöglichkeiten
choice = input("Welche Tür? (links/rechts/geradeaus): ").strip().lower()

# Idee 2: Spieler nach Namen fragen
name = input("Wie heißt du? ")
print(f"Willkommen {name} zu deinem Abenteuer!")

# Idee 3: Zufällige Ereignisse
import random
if random.randint(1, 2) == 1:
    print("Du hast Glück!")
else:
    print("Pech gehabt!")

# Idee 4: Punkte zählen
score = 0
score += 10
print(f"Deine Punkte: {score}")
```

**Probiere aus**: Nimm eine Idee und baue sie in das Spiel ein!

## Teil 2: Was ist Git und warum brauchen wir es?

### Das Problem ohne Versionskontrolle

Stell dir vor, du arbeitest an einem Programm:

- **Tag 1**: Du schreibst 50 Zeilen Code
- **Tag 2**: Du fügst 20 Zeilen hinzu, aber etwas funktioniert nicht mehr
- **Tag 3**: Du willst zu Tag 1 zurück, aber hast die alte Version überschrieben

**Ohne Git**: Du verlierst deine Arbeit!

**Mit Git**: Du kannst jederzeit zu jeder Version zurückkehren!

### Was Git löst

- **Versionskontrolle**: Alle Änderungen werden gespeichert
- **Backup**: Dein Code ist sicher auf GitHub
- **Zusammenarbeit**: Mehrere Personen können am gleichen Projekt arbeiten
- **Nachverfolgung**: Du siehst, wer was wann geändert hat

## Teil 3: Git Grundbegriffe erklärt

### Repository (Repo)

Ein **Repository** ist wie ein Ordner für dein Projekt mit Gedächtnis:

```text
Mein-Projekt/
├── main.py
├── README.md
├── .git/           ← Git-Gedächtnis (versteckt)
```

### Commit

Ein **Commit** ist wie ein Foto deines Codes zu einem bestimmten Zeitpunkt:

```text
Commit 1: "Erstes Text-Adventure erstellt"
Commit 2: "Lebenspunkte hinzugefügt"
Commit 3: "Bug im Kampfsystem behoben"
```

**Analogie**: Wie Speicherstände in einem Videospiel!

### Remote Repository

Ein **Remote Repository** (z.B. auf GitHub) ist eine Kopie deines Projekts im Internet:

```text
Dein Computer (lokal)     GitHub (remote)
├── main.py          ←→   ├── main.py
├── README.md        ←→   ├── README.md
```

## Teil 4: Die wichtigsten Git-Befehle

### Push - Code hochladen

```bash
git push
```

**Was passiert**: Deine lokalen Commits werden zu GitHub hochgeladen

**Analogie**: Wie Fotos von deinem Handy zu Google Photos hochladen

### Pull - Änderungen herunterladen

```bash
git pull
```

**Was passiert**: Neue Commits von GitHub werden zu dir heruntergeladen

**Analogie**: Wie WhatsApp-Nachrichten empfangen

### Fetch - Nur schauen, nicht ändern

```bash
git fetch
```

**Was passiert**: Git schaut nach neuen Commits, lädt sie aber nicht herunter

**Analogie**: Wie die Vorschau von E-Mails lesen, ohne sie zu öffnen

### Add & Commit - Änderungen speichern

```bash
git add .
git commit -m "Beschreibung der Änderung"
```

**Was passiert**:

1. `add`: Dateien für Commit vorbereiten
2. `commit`: Einen neuen Speicherstand erstellen

## Teil 5: Branches - Parallele Entwicklung

### Was sind Branches?

**Branches** sind wie parallele Universen für deinen Code:

```text
main Branch:     A---B---C---D
                     |
feature Branch:      E---F---G
```

### Warum Branches?

Beispiel: Du willst ein neues Feature testen

Main -------------------> Main Branch: Funktionierendes Spiel
          ↓
        Feature ---> Feature Branch: Spiel mit Musik

- Wenn Musik gut ist → Feature in Main integrieren
- Wenn Musik schlecht ist → Feature Branch löschen

### Branch-Befehle

```bash
# Neuen Branch erstellen
git branch feature-musik

# Zu Branch wechseln
git checkout feature-musik

# Oder beides in einem Befehl
git checkout -b feature-musik
```

## Teil 6: Fork - Projekt kopieren

### Was ist ein Fork?

Ein **Fork** ist deine eigene Kopie von jemand anderem Projekt:

```text
Original Projekt (nicht deins)
        ↓ Fork
Deine Kopie (komplett unter deiner Kontrolle)
```

### Warum Forken?

- Du willst ein Open-Source-Projekt verbessern
- Du willst experimentieren, ohne das Original zu stören
- Du willst ein Projekt als Basis für dein eigenes nutzen

## Teil 7: Git-Workflow in der Praxis

### Schritt-für-Schritt Git-Workflow

Da wir bereits ein Fork vom Python-Praktikum haben, können wir direkt mit dem Git-Workflow loslegen:

1. **Änderungen am Spiel machen**

   ```bash
   # Öffne main.py und verbessere das Text-Adventure
   # Probiere eine der Ideen von oben aus
   ```

2. **Änderungen committen**

   ```bash
   git add main.py
   git commit -m "Text-Adventure erweitert: Name-Abfrage hinzugefügt"
   ```

3. **Zu GitHub hochladen**

   ```bash
   git push
   ```

4. **Neue Änderungen von anderen holen** (falls jemand anderes am Projekt arbeitet)

   ```bash
   git pull
   ```

5. **Den aktuellen Status prüfen**

   ```bash
   git status
   ```

**Wichtig**: Ein Ansprechpartner hilft dir gerne, wenn Git-Befehle nicht funktionieren!

### Aufgabe 1: Text-Adventure erweitern

Öffne die `main.py` und erweitere das Text-Adventure um eine weitere Entscheidung:

- Füge eine dritte Tür "geradeaus" hinzu
- Lass den Spieler nach seinem Namen fragen
- Verwende den Namen in der Begrüßung

**Erfolgskriterium**: Das Spiel hat drei Türen und begrüßt den Spieler mit Namen.

### Aufgabe 2: Git-Workflow üben

Wende den kompletten Git-Workflow auf deine Änderungen an:

- Teste deine Änderungen lokal mit `python main.py`
- Erstelle einen aussagekräftigen Commit mit deinen Verbesserungen
- Lade deine Änderungen zu GitHub hoch
- Prüfe auf GitHub, ob deine Änderungen angekommen sind

**Erfolgskriterium**: Deine Änderungen sind auf GitHub sichtbar und haben eine gute Commit-Message.

### Aufgabe 3: Eigene Funktion schreiben

Erstelle eine neue Funktion `zeige_inventar()` in der `main.py`:

- Die Funktion soll eine Liste von Gegenständen ausgeben
- Verwende die Funktion im Spiel, wenn der Spieler einen Schatz findet
- Experimentiere mit verschiedenen Gegenständen

**Erfolgskriterium**: Eine funktionierende Funktion, die das Inventar anzeigt und im Spiel verwendet wird.

## Teil 8: Git-Befehle Übersicht

| Befehl                | Was es macht                | Wann nutzen                              |
| --------------------- | --------------------------- | ---------------------------------------- |
| `git init`            | Neues Repository erstellen  | Zu Beginn eines Projekts                 |
| `git add .`           | Alle Änderungen vorbereiten | Vor jedem Commit                         |
| `git commit -m "..."` | Speicherstand erstellen     | Nach wichtigen Änderungen                |
| `git push`            | Zu GitHub hochladen         | Um Arbeit zu sichern                     |
| `git pull`            | Von GitHub herunterladen    | Vor dem Arbeiten                         |
| `git status`          | Aktueller Zustand           | Um zu sehen, was passiert ist            |
| `git log`             | Historie anzeigen           | Um alte Commits zu finden                |
| `git branch`          | Branches anzeigen           | Um zu sehen, wo du bist                  |
| `git checkout`        | Branch wechseln             | Um an verschiedenen Features zu arbeiten |

## Lernziele Check

Nach diesem Tag solltest du:

- ✅ Das Text-Adventure verstehen und erweitern können
- ✅ Wissen, warum Git wichtig ist
- ✅ Den Unterschied zwischen commit, push, pull, fetch kennen
- ✅ Verstehen, was Branches und Forks sind
- ✅ Einen einfachen Git-Workflow anwenden können

## Tipps

- **Kleine Commits**: Committe oft, aber nur zusammengehörige Änderungen
- **Gute Commit-Messages**: "Bug behoben" ist schlecht, "Rechenfehler in Punkteberechnung behoben" ist gut
- **Backup-Mentalität**: Push regelmäßig zu GitHub - so ist dein Code immer sicher
- **Experimentierfreude**: Branches sind sicher zum Experimentieren
- **Fehler sind normal**: Git kann fast alles rückgängig machen - hab keine Angst!
- **Frag nach Hilfe**: Ein Ansprechpartner ist immer da, wenn Git verwirrt

## Perfekt gemacht

Du hast heute zwei wichtige Meilensteine erreicht: Du kannst jetzt eigene Funktionen schreiben UND mit Git arbeiten! Das sind fundamentale Fähigkeiten, die dir in deiner gesamten Programmier-Laufbahn helfen werden.

Git mag am Anfang kompliziert wirken, aber mit der Zeit wird es zur zweiten Natur. Du hast heute die wichtigsten Befehle kennengelernt und kannst deinen Code sicher verwalten. Das Text-Adventure zeigt, wie aus einfachen Python-Konzepten richtige Programme entstehen.

Morgen geht es weiter mit PyTorch und Bilderkennung - ein großer Sprung in die Welt des maschinellen Lernens! Bis dahin: Experimentiere gerne mit dem Text-Adventure und übe den Git-Workflow. Du machst große Fortschritte!
