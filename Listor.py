games = []

while True:

    menu = input("Val: ")

    if menu == "1":
        for l in games:
            print(l)
    elif menu == "2":
        games ={}
        games ["company"] = input ("Company: ")
        games ["game"]    = input ("Game: ")
        games["year"] = int(input("Year"))

        games.append(games)
    elif menu == "3":
        for l in "games":
            if "games" in l:
                print("game exists!")
    elif menu == "4":
        with open('games.txt' , 'a+') as f:
            for game in games:
                f.write(str(game))
        f.close()
    else:
        break

