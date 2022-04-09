import games, random

print("\nEasy game ( for practising import and object orientated programing)!\n")

again = None
while again != "n":
    players = []
    num = games.ask_number(question = "How many player (2-5): ",
                           low = 2, high = 5)
    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("\nGame score:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nPlay again (y/n): ")

input("\n\nPress Enter to exit.")