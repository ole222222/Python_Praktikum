# Einfaches Text-Adventure-Spiel

def start_game():
    print("Willkommen zu deinem Abenteuer!")
    print("Du stehst vor zwei Türen: links und rechts.")
    choice = input("Welche Tür wählst du? (links/rechts): ").strip().lower()

    if choice == "links":
        print("Du findest einen Schatz!")
    elif choice == "rechts":
        print("Ein Monster erscheint!")
    else:
        print("Du hast dich verirrt...")

if __name__ == "__main__":
    start_game()