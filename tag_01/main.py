# Willkommen zu deinem ersten Python-Projekt!

print()
print("="*20)
print()
# Variablen und Datentypen
name = "Ole"
alter = 15
print("Hallo", name, "- du bist", alter, "Jahre alt.")

# Bedingungen
if alter >= 14:
    print("Du bist alt genug für dieses Praktikum!")
else:
    print("Du bist noch zu jung.")
# 🎮 Teil 4: Zahlenraten-Spiel
import random

print()
print("="*20)
print()
geheime_zahl = random.randint(1, 2)
versuche = 0
print("Ich denke an eine Zahl zwischen 1 und 20. Kannst du sie erraten?")

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

#Rechner
print()
print("="*20)
print()
print("Nenne 2 Zahlen")
Zahl1 = int(input())
Zahl2 = int(input())
summeA = Zahl2 + Zahl1
summeS = Zahl1 - Zahl2
summeM = Zahl1 * Zahl2
summeD = Zahl1 / Zahl2
print("Summe Addition ", summeA)
print("Summe Subtraktion", summeS)
print("Summe Multiplikation", summeM)
print("Summe Division",summeD)

#Primzahlen
print()
print("="*20)
print()
print("Gib eine Zahl ein")
Zahl1 = int(input())
xAnzahl=0
for i in range(1,Zahl1):
    print(i) 
    for x in range(1, i -1):
        if i % x ==0:
            if x<i :
                if x>1 :
                    xAnzahl +=1
                    if xAnzahl>2:
                        print(i, "ist keine Primzahl")
                    
           
                    if xAnzahl== 2:
                        print(i,"ist eine Primzahl")           
                        break     