# Simple Command-Line RPG Game
# Internship Project - Main Flow Services and Technologies

import random

player = {"name": "Hero", "health": 100, "attack": 15}
enemy = {"name": "Dragon", "health": 80, "attack": 10}

print("Welcome to the RPG Game!")
print(f"You are {player['name']} battling a {enemy['name']}!")

while player["health"] > 0 and enemy["health"] > 0:
    action = input("\nChoose Action (attack/heal/run): ").lower()
    if action == "attack":
        damage = random.randint(10, player["attack"])
        enemy["health"] -= damage
        print(f"You attacked {enemy['name']} for {damage} damage!")
    elif action == "heal":
        heal = random.randint(5, 15)
        player["health"] += heal
        print(f"You healed yourself for {heal} health!")
    elif action == "run":
        print("You ran away safely!")
        break
    else:
        print("Invalid action!")

    if enemy["health"] > 0:
        damage = random.randint(5, enemy["attack"])
        player["health"] -= damage
        print(f"{enemy['name']} attacked you for {damage} damage!")

    print(f"Your Health: {player['health']} | Enemy Health: {enemy['health']}")

if player["health"] <= 0:
    print("\nYou were defeated by the Dragon!")
elif enemy["health"] <= 0:
    print("\nCongratulations! You defeated the Dragon!")
