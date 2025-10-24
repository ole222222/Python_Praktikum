# Tag 5: KI-Text-Adventure mit Ollama-LLM

Willkommen zum großen Finale deines Python-Praktikums! Heute erweitern wir das einfache Text-Adventure aus Tag 2 mit echter Künstlicher Intelligenz. Statt vordefinierter Antworten erschaffst du ein Spiel, das kreativ und dynamisch auf deine Eingaben reagiert. Das ist der Sprung von statischer Programmierung zu intelligenten, adaptiven Anwendungen!

## Was du heute machst

Du baust ein intelligentes Text-Adventure, das einen lokalen KI-Server (Ollama) nutzt. Dabei lernst du:

- **Ollama einrichten**: Lokalen KI-Server installieren und konfigurieren
- **Python-Bibliotheken nutzen**: Einfache Integration mit der ollama-python Lib
- **System-Prompts schreiben**: Der KI eine Rolle und Persönlichkeit geben
- **Chat-Verlauf verwalten**: Gespräche mit Gedächtnis und Kontext führen
- **Intelligente Anwendungen**: Von statischen zu adaptiven Programmen

## Grundlagen: Was ist Ollama?

Ollama ist ein Tool, das dir ermöglicht, große Sprachmodelle (wie ChatGPT) lokal auf deinem Computer auszuführen. Das bedeutet:

- **Kostenlos**: Keine teuren API-Kosten
- **Privat**: Deine Daten bleiben auf deinem Computer
- **Offline**: Funktioniert ohne Internetverbindung
- **Flexibel**: Verschiedene Modelle für verschiedene Zwecke

### Python-Bibliothek für Ollama

Statt komplizierte HTTP-Requests zu schreiben, nutzen wir die offizielle `ollama` Python-Bibliothek:

```python
import ollama

def teste_ollama_verbindung():
    """Prüft ob Ollama läuft und zeigt verfügbare Modelle"""
    try:
        modelle = ollama.list()
        print("Ollama läuft! Verfügbare Modelle:")
        for modell in modelle['models']:
            print(f"- {modell['name']}")
        return True
    except Exception as fehler:
        print(f"Ollama ist nicht erreichbar: {fehler}")
        return False

def einfache_frage(nachricht, modell="llama2"):
    """Stellt eine einfache Frage an Ollama"""
    try:
        antwort = ollama.generate(
            model=modell,
            prompt=nachricht
        )
        return antwort['response']
    except Exception as fehler:
        return f"Fehler: {fehler}"

# Beispiel
antwort = einfache_frage("Erkläre Python in einem Satz.")
print(antwort)
```

**Installation der Ollama-Bibliothek:**

```powershell
pip install ollama
```

### System-Prompts: Der KI eine Rolle geben

System-Prompts sind spezielle Anweisungen, die definieren, wie sich die KI verhalten soll. Sie funktionieren wie ein "Rollenbuch" für einen Schauspieler.

**Grundprinzip eines System-Prompts:**

```python
# Basis-Struktur für einen System-Prompt
system_prompt = """Du bist [WER/WAS].

Deine Eigenschaften:
- [Eigenschaft 1]
- [Eigenschaft 2] 
- [Eigenschaft 3]

Dein Verhalten:
- [Wie du antwortest]
- [Was du tust]
- [Was du vermeidest]

Dein Stil:
- [Antwortlänge]
- [Tonfall]
- [Spezielle Ausdrücke]"""
```

**Beispiel: Einfacher Tutor**

```python
TUTOR_PROMPT = """Du bist ein geduldiger Programmier-Tutor.

Deine Eigenschaften:
- Erklärst Konzepte einfach und verständlich
- Bist geduldig mit Anfängern
- Nutzt praktische Beispiele

Dein Verhalten:
- Antworte in 1-2 Sätzen
- Stelle Rückfragen wenn etwas unklar ist
- Ermutige den Lernenden

Dein Stil:
- Freundlich und unterstützend
- Nutze einfache Sprache
- Sage "Lass mich das erklären..." wenn du beginnst"""

def frage_tutor(frage):
    antwort = ollama.generate(
        model="llama2",
        prompt=f"{TUTOR_PROMPT}\n\nFrage: {frage}\n\nTutor:"
    )
    return antwort['response']
```

**Deine Aufgabe:** Experimentiere mit verschiedenen Rollen! Versuche einen Piraten-Kapitän, einen Wissenschaftler oder einen mittelalterlichen Ritter zu erschaffen.

### Chat-Verlauf für Gedächtnis

Damit die KI sich an vorherige Nachrichten erinnert, nutzen wir die Chat-Funktion:

```python
def chat_mit_gedaechtnis():
    """Führt ein Gespräch mit Gedächtnis"""
    
    nachrichten = []  # Hier wird alles gespeichert
    system_prompt = "Du bist ein hilfsbereiter Assistent."
    
    print("Chat gestartet! (Schreibe 'quit' zum Beenden)")
    
    while True:
        benutzer_eingabe = input("Du: ")
        
        if benutzer_eingabe.lower() == 'quit':
            break
        
        # Füge neue Nachricht hinzu
        nachrichten.append({
            'role': 'user',
            'content': benutzer_eingabe
        })
        
        # Hole Antwort von Ollama
        antwort = ollama.chat(
            model='llama2',
            messages=[
                {'role': 'system', 'content': system_prompt}
            ] + nachrichten
        )
        
        ai_antwort = antwort['message']['content']
        print(f"KI: {ai_antwort}")
        
        # Speichere KI-Antwort auch
        nachrichten.append({
            'role': 'assistant', 
            'content': ai_antwort
        })
        
        # Verlauf kürzen wenn zu lang
        if len(nachrichten) > 10:
            nachrichten = nachrichten[-10:]
```

### Vollständiges Adventure-Beispiel

```python
def ki_adventure():
    """Text-Adventure mit KI-Spielleiter"""
    
    # Dein System-Prompt hier - erstelle einen Spielleiter!
    spielleiter_prompt = """[Hier kommt dein System-Prompt für den Spielleiter]"""
    
    nachrichten = []
    
    print("Willkommen zu deinem KI-Adventure!")
    
    # Spiel starten
    start_nachricht = "Beginne ein spannendes Adventure. Beschreibe den Startort."
    
    antwort = ollama.chat(
        model='llama2',
        messages=[
            {'role': 'system', 'content': spielleiter_prompt},
            {'role': 'user', 'content': start_nachricht}
        ]
    )
    
    print(f"Spielleiter: {antwort['message']['content']}")
    
    # Hauptspiel-Schleife
    while True:
        aktion = input("\nWas machst du? ")
        
        if aktion.lower() == 'quit':
            break
        
        nachrichten.append({'role': 'user', 'content': aktion})
        
        antwort = ollama.chat(
            model='llama2',
            messages=[
                {'role': 'system', 'content': spielleiter_prompt}
            ] + nachrichten
        )
        
        ai_antwort = antwort['message']['content']
        print(f"Spielleiter: {ai_antwort}")
        
        nachrichten.append({'role': 'assistant', 'content': ai_antwort})
```

## Aufgaben für Tag 5

### Aufgabe 1: Ollama-Verbindung testen

Erstelle ein Programm `ollama_test.py`, das:

- Prüft ob Ollama läuft und zeigt verfügbare Modelle
- Stellt eine einfache Frage und zeigt die Antwort
- Testet verschiedene Fragen und vergleicht Antworten
- Bei Fehlern hilfreiche Meldungen zeigt

**Erfolgs-Kriterium:** Dein Programm kann mit Ollama kommunizieren und zeigt alle verfügbaren Modelle an.

### Aufgabe 2: System-Prompt Experimente

Baue ein `system_prompt_test.py` mit:

- Mindestens 3 verschiedenen Charakteren (z.B. Pirat, Wissenschaftler, Ritter)
- Jeder Charakter hat einen eigenen System-Prompt nach dem gelernten Schema
- Benutzer kann zwischen Charakteren wechseln
- Teste denselben Satz bei verschiedenen Charakteren

**Erfolgs-Kriterium:** Jeder Charakter antwortet deutlich unterschiedlich und bleibt in seiner Rolle.

### Aufgabe 3: Intelligentes Text-Adventure

Erweitere das Text-Adventure aus Tag 2 zu einem `ki_adventure.py`:

- Nutzt einen selbst erstellten Spielleiter-System-Prompt
- Erinnert sich an alle vorherigen Aktionen mit Chat-Verlauf
- Reagiert kreativ auf unerwartete Spieler-Eingaben
- Hat einen spannenden Startpunkt und entwickelt sich dynamisch

**Erfolgs-Kriterium:** Das Adventure erzählt eine zusammenhängende Geschichte, die sich an deine Aktionen erinnert.

## Lernziel Check

Nach Tag 5 kannst du:

- [ ] Ollama installieren und konfigurieren
- [ ] Die ollama-python Bibliothek nutzen für einfache KI-Integration
- [ ] System-Prompts nach dem gelernten Schema schreiben
- [ ] Chat-Verläufe verwalten für längere Unterhaltungen
- [ ] Verschiedene KI-Charaktere mit unterschiedlichen Persönlichkeiten erstellen
- [ ] Ein intelligentes Text-Adventure programmieren das sich an alles erinnert
- [ ] Fehlerbehandlung für KI-Verbindungen implementieren
- [ ] Den Unterschied zwischen statischen und adaptiven Programmen verstehen

## Tipps

**Ollama-Probleme?**

- Prüfe ob der Server läuft: `ollama serve` in PowerShell
- Teste die Verbindung: `ollama list` in PowerShell zeigt Modelle
- Falls Modell fehlt: `ollama pull llama2` installiert es

**System-Prompts verbessern:**

- Sei spezifisch: "Du antwortest in 2 Sätzen" statt "Du bist hilfreich"
- Gib Beispiele für gewünschtes Verhalten im Prompt
- Definiere was die KI NICHT tun soll

**Chat-Verlauf optimieren:**

- Zu lange Verläufe können langsam werden
- Behalte die wichtigsten Nachrichten und lösche ältere
- System-Prompts immer am Anfang der Nachrichtenliste

**Debugging-Tipp:**
Wenn etwas nicht funktioniert, teste jeden Schritt einzeln: Verbindung → Einfache Frage → System-Prompt → Chat-Verlauf

Du bist nicht allein! Bei Problemen mit Ollama, System-Prompts oder der Python-Integration ist immer jemand da, der dir hilft. KI-Programmierung kann am Anfang verwirrend sein - frag ruhig nach!

## Herzlichen Glückwunsch

Du hast gerade den Sprung von traditioneller Programmierung zu KI-gestützten Anwendungen geschafft! Das was du heute gelernt hast - Kommunikation mit Sprachmodellen, Python-Bibliotheken für KI und intelligente Systeme - sind Fähigkeiten, die in der modernen Softwareentwicklung extrem wertvoll sind.

Dein Text-Adventure ist nicht nur ein Spiel, sondern der Grundstein für alle möglichen intelligenten Anwendungen: Chatbots, Assistenten, kreative Tools und vieles mehr. Du hast die Grundlagen für die Zukunft der Programmierung gelernt!