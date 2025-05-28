# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

#global scope

# player_healt = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_healt)

# drink_potion()

game_level = 3
enemies = ["Skieleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)