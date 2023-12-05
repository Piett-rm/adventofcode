maxColor = {
    "red": 12,
    "green":13,
    "blue": 14,
}


tab = set()
total = 0
with open("2d.txt", "r") as fichier:
    for ligne in fichier.read().splitlines():
        power= {
            "red":0,
            "green":0,
            "blue": 0,
        }
        games = ligne.split(":")
        numberGame = games[0].split(" ")
        color_with_numbers = games[1].replace(";",",").split(",")
        for color_with_number in color_with_numbers:
            tirage = color_with_number.strip().split(" ")
            number = tirage[0]
            color = tirage[1]
            if int(number) > power[color]:
                power[color] = int(number)
            # part 1
            # if int(number) <= maxColor[color]:
            #     tab.add(int(numberGame[1]))
            # else:
            #     if int(numberGame[1]) in tab:
            #         tab.remove(int(numberGame[1]))
            #     break
        power_ligne = power["red"] * power["green"] * power["blue"]
        total += power_ligne                
##sum du tab
# print(sum(tab))
print(total)