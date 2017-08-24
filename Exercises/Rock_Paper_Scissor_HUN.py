import random
def mainGame():
    options = ["kő", "papír", "olló"]
    userInput = input("Kérlek válassz fegyvert! Kő, papír vagy olló!: ").lower()
    AI = random.choice(options)
    if userInput == "kő" or userInput == "papír" or userInput == "olló":
        if userInput == AI:
                print("Döntetlen :p")
                replay()
        if userInput == "kő":
            if AI == "papír":
                print("Számítógép nyert! Papír > kő")
                replay()
        if userInput == "papír":
            if AI == "olló":
                print("Számítógép nyert! Olló > papír")
                replay()
        if userInput == "olló":
            if AI == "kő":
                print("Számítógép nyert! Kő > olló")
                replay()
        if userInput == "olló":
            if AI == "papír":
                print("Ön nyert! Olló > papír")
                replay()
        if userInput == "papír":
            if AI == "kő":
                print("Ön nyert! Papír > kő")
                replay()
        if userInput == "kő":
            if AI == "olló":
                print("Ön nyert! Kő > olló")
                replay()
    else:
        print("Nem érvényes fegyver.")
def replay():
    newgame = input("Szeretnél ismét játszani?(i/n): ").lower()
    if newgame == "i":
        mainGame()
    elif newgame == "n":
        print("Viszlát")
    else:
        print("Nem érvényes fegyver.")
        replay()
mainGame()
