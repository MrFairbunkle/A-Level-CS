import random
import time # add timer for sword guy screen to start game
# screen_wdth = 100%

print("   _____                      _    _____\n  / ____|                    | |  / ____|\n | (_____      _____  _ __ __| | | |  __ _   _ _   _\n  \___ \ \ /\ / / _ \| '__/ _` | | | |_ | | | | | | |\n  ____) \ V  V / (_) | | | (_| | | |__| | |_| | |_| |\n |_____/ \_/\_/ \___/|_|  \__,_|  \_____|\__,_|\__, |\n                                                __/ |\n                                               |___/ ")
print("\nWelcome to Sword Guy, the turn based adventure RPG where the only limit to power is your patience.\n")

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100 # physical damage the player can withstand
        self.attack = 10 # physical damage done by the player's attacks
        self.defense = 5 # lowers the taken damage by 1 for each 1 defence

    def display_stats(self):
        print(f"{self.name}'s Stats - \nHealth: {self.health}\n Attack: {self.attack}\n Defense: {self.defense}")

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")
        
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def display_stats(self):
        print(f"{self.name}'s Stats - \nHealth: {self.health}\n Attack: {self.attack}\n Defense: {self.defense}")

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")

def battle(player, enemy):
    print("Battle Start!")
    player.display_stats()
    enemy.display_stats()

    while player.health > 0 and enemy.health > 0:
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        enemy.attack_player(player)
        if player.health <= 0:
            print("Game Over! You have been defeated.")
            break

        print("\n--- Next Turn ---\n")

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    enemy1 = Enemy("Goblin", 30, 8, 3)
    enemy2 = Enemy("Orc", 40, 10, 5)

    items = {
        'Sword': {'attack': 5},
        'Shield': {'defense': 3},
    }

    while True:
        print("\n1. Display Player Stats")
        print("2. Battle Goblin")
        print("3. Battle Orc")
        print("4. Pick up Sword")
        print("5. Pick up Shield")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            player.display_stats()

        elif choice == '2':
            battle(player, enemy1)

        elif choice == '3':
            battle(player, enemy2)

        elif choice == '4':
            player.attack += items['Sword']['attack']
            print("You picked up a Sword! Your attack has increased.")

        elif choice == '5':
            player.defense += items['Shield']['defense']
            print("You picked up a Shield! Your defense has increased.")

        elif choice == '6':
            print("Goodbye! Thanks for playing.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()