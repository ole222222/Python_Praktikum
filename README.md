# Python Praktikum

Ein Repository, das Praktikant*innen **ohne Vorkenntnisse** die Programmiersprache **Python** Schritt fur Schritt näherbringt.  
Diese Anleitung zeigt genau, wie du deine Entwicklungsumgebung unter **Windows** einrichtest, das Repository klonst und das Praktikum startest.

## Vorbereitung

Wenn dir ein Schritt unklar ist, frage bitte nach das ist ausdrücklich erwünscht!

### 1. Fork des Repositories (auf GitHub)

1. Öffne deinen Web-Browser und gehe zur GitHub-Seite dieses Repositories.  
2. Melde dich mit deinem GitHub-Account an (oder erstelle einen neuen Account).  
3. Klicke oben rechts auf **Fork**.  
   GitHub erstellt eine **Kopie des Repositories in deinem Account**:  
   `https://github.com/<dein-nutzername>/Python_Praktikum`

### 2. Tools installieren

Du brauchst drei Programme:

- Visual Studio Code
- Python 3.x
- Git

#### Visual Studio Code (VS Code)

1. Gehe zu [https://code.visualstudio.com/](https://code.visualstudio.com/).  
2. Klicke auf **Download for Windows** und starte die Installationsdatei.  
3. Wähle während der Installation:
   - Add to PATH
   - Open with Code im Kontextmenü
4. Installation abschließen.

#### Python 3.x installieren

1. Gehe zu [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).  
2. Lade die aktuelle Version (z. B. 3.11 oder 3.12) herunter.  
3. Aktiviere beim Installieren die Option
   - add Python 3.x to PATH
4. Wähle **Install Now**.  
5. Prüfe die Installation:
   ```powershell
   python --version
   ```
   Ausgabe sollte z. B. `Python 3.xx.x` sein.

#### Git installieren

1. Gehe zu [https://git-scm.com/download/win](https://git-scm.com/download/win).  
2. Lade den Installer herunter und starte ihn.  
3. Bei der Frage "Adjusting your PATH environment" wähle:  
   **Git from the command line and also from 3rd-party software**  
4. Nach der Installation prüfen:
   ```powershell
   git --version
   ```
   Beispielausgabe: `git version 2.xx.x`

### Dein geforktes Repository klonen (auf den PC holen)

1. öffne deinen Fork auf GitHub:  

### Projekt in VS Code öffnen

1. Starte Visual Studio Code.
2. Klicke auf **Datei** > **Ordner öffnen** und wähle den Ordner deines geklonten Repositories aus.

### Virtuelle Umgebung anlegen (empfohlen)

1. Öffne das Terminal in VS Code: **Terminal** > **Neues Terminal**.
2. Erstelle eine virtuelle Umgebung:
   ```powershell
   python -m venv venv
   ```
3. Aktiviere die virtuelle Umgebung:
   - Windows:
     ```powershell
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Erste Datei ausführen (Start von Tag 1)

1. Öffne die Datei `tag_01_python_basics/main.py` in VS Code.
2. Drücke `F5` oder klicke auf **Run Python File** oben rechts.
