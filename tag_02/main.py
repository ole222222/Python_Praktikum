# Einfaches Text-Adventure-Spiel

def start_game():
    import random
    score = 0
    name = input("Wie heißt du? ")
    print(f"Willkommen {name} zu deinem Abenteuer!")
    print("Du stehst vor zwei Türen: links und rechts.")
    choice = input("Welche Tür wählst du? (links/rechts): ").strip().lower()
    if choice == "links":
        print("Du findest einen Schatz!")
    elif choice == "rechst":
        if random.randint(1, 5) == 1:
            print("Du hast Glück!")
        else:
            print("Du hast Pech, ein Monster erscheint!") 
            choice = input("Kämpfen oder Weglaufen?")
            if choice == "Kämpfen":
                if random.randint(1, 3) == 1:
                    print("du hast gewonnen!")
                    score += 10
                    print(f"Deine Punkte: {score}")
                else :
                    print("Du hast verloren!")
                    score -=10 
                    print("-10 Punkte:", score)
    if choice == "links":
        print("Du hast einen Schatz gefunden!")
        score +=10
        print("+10 Punkte")                                            
    else:
        if random.randint(1, 20) == 1:
            print("Du hast einen Schatz gefunden!")
            score += 10
            print(f"Deine Punkte: {score}")
        else:
            print("Du hast dich verirrt...")
    print("Du hast zwei weitere Türen gefunden, eine links und eine rechts") 
    choice = input("Welche Tür wählst du? (links/rechts): ").strip().lower() 
    if choice == "links":
        print("Du siehst ein Monster!") 
        choice = input("Kämpfen oder Weglaufen?")
        if choice == "Kämpfen":
            if random.randint(1, 3) == 1:
                print("du hast gewonnen!")
                score += 10
                print(f"Deine Punkte: {score}")
            else :
                print("Du hast verloren!")
                score -=10 
                print("-10 Punkte:", score)   
        elif choice == "Weglaufen" :
            if random.randint(1, 2) == 1:
                print("Du bist weggekommen!")
            else :
                print("Du bist nicht weggekommen, du hast verloren!")    
    if choice == "rechts":
        print("Du hast einen Schatz gefunden!")
        score +=10
        print("+10 Punkte")        

if __name__ == "__main__":
    start_game()
