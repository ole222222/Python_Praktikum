# Willkommen zu deinem ersten Python-Projekt!

# 🐍 Teil 1: Variablen und Datentypen
name = "Hans"
alter = 17
print("Hallo", name, "- du bist", alter, "Jahre alt.")

# 🧮 Teil 2: Bedingungen
if alter >= 14:
    print("Du bist alt genug für dieses Praktikum!")
else:
    print("Du bist noch zu jung.")

# 🔁 Teil 3: Schleifen
for i in range(5):
    print("Dies ist Schleife Nummer", i + 1)

# 🎮 Teil 4: Zahlenraten-Spiel
import random

geheime_zahl = random.randint(1, 10)
versuche = 0
print("Ich denke an eine Zahl zwischen 1 und 10. Kannst du sie erraten?")

while True:
    tipp = int(input("Dein Tipp: "))
    versuche += 1
    if tipp == geheime_zahl:
        print("Richtig! Du hast", versuche, "Versuche gebraucht.")
        break
    elif tipp < geheime_zahl:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")
