dict = {
    "red": 0,
    "bleu": 0,
    "green": 0
}

with open("2d.txt", "r") as fichier:
    for ligne in fichier.read().splitlines():
        games = ligne.split(":")
        color_with_numbers = games[1].replace(";",",").split(",")
        for color_with_number in color_with_numbers:
            tirage = color_with_number.strip().split(" ")
            number = tirage[0]
            color = tirage[1]

        # for lettre in ligne:
        #     if lettre.isnumeric():
        #         print(lettre)
        #         tab.append(int(lettre))
      
