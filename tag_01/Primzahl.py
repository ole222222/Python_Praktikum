#Primzahlen
print()
print("="*20)
print()
print("Gib eine Zahl ein")
Zahl1 = int(input())
for i in range(1,Zahl1): 
    xAnzahl=0
    for x in range(1, i -1):
        if i % x ==0:
            xAnzahl +=1
    
    if xAnzahl<=1 :
        print(i,"ist eine Primzahl")               
        