# Einfaches Text-Adventure-Spiel
import random

score = 0
Gold = 0


# def zeige_inventar() : 
#     Gold = 0  
#     choice = input("Inventar öffnen? Ja/Nein")
#     if choice == "Ja" :
#         print("Gold :",Gold) 
#     elif choice == "Nein":
#         print()


def tür_wahl() :
    global Gold
    wahl = input("Welche Tür wählst du? (links/rechts): ").strip().lower()
    if wahl == "links" or wahl == "rechts" :
        rand = random.randrange(0,300) % 2
        if rand == 1 :
            print("Du hast einen Schatz gefunden !")
            print("Gold + 10")
            Gold += 10
            tür_wahl()
        else :
            print("Du findest ein Monster!")
            monster()
            tür_wahl()
    else :
        print("done")
        return

def monster():
    global score
    global Gold
    choice = input("Möchtest du gegen das Monster Kämpfen oder Fliehen? : ").strip().lower()
    if choice == "kämpfen":
        rand =random.randrange(0,300) % 2
        if rand== 1 :
            print("Du hast den Kampf gewonnen!")
            score += 10 
            print("Score + 10")   
            if score == 50 :
                print("Du hast gewonnen!  Dein Score:", score)
                print("Dein Gold :", Gold)
                score -= score
                Gold -= Gold
                start_game()
        else :
            print("Du hast verloren")
            Gold -= 10
            print("Gold -10")
    elif choice == "fliehen" :
        print("Du bist geflohen!")
    else : 
        monster()


def start_game():
    name = input("Wie heißt du? ")
    print(f"Willkommen {name} zu deinem Abenteuer!")
    tür_wahl()
   

if __name__ == "__main__":
    start_game()
