print("Welcome to the secret auction program!")
players = {}

while(True):
    user = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    players[f"{user}"] = bid_price
    next_player = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if next_player == "yes":
        print("\n"*100)
    elif next_player == "no":
        max_bid = max(players, key=players.get)
        print(f"The winner is {max_bid} with a bid of ${players[max_bid]}.")
        break
