import random
import time # add timer for sword guy screen to start game
# screen_width = 100%
# screen_height = 100%

print("   _____                      _    _____\n  / ____|                    | |  / ____|\n | (_____      _____  _ __ __| | | |  __ _   _ _   _\n  \___ \ \ /\ / / _ \| '__/ _` | | | |_ | | | | | | |\n  ____) \ V  V / (_) | | | (_| | | |__| | |_| | |_| |\n |_____/ \_/\_/ \___/|_|  \__,_|  \_____|\__,_|\__, |\n                                                __/ |\n                                               |___/ ")
print("\nWelcome to Sword Guy, the turn based adventure RPG where the only limit to power is your patience.\n")


sword_found=False
shield_found=False

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







turns=0
healPots=3
manaPots=3

def combat(x, y):
    global turns
    
    while Player.health > 0 and Enemy.health > 0:
        diceRollArray = []
        
        for i in range(5):
            diceRollArray.append(random.randint(1, 6))

        choice=input("Do you want to: A. take your turn, or B. use an item? ")
        choice=choice.upper()
        if choice=="A":
            total = sum(diceRollArray)
            print(f"Turn {turns+1}")
            print(f"You rolled {diceRollArray} and got a total of {total}.")
            
            if total < 20:
                Player.health -= 10
                print(f"Player lost 10 health and now has {Player.health} health left.\n")
            else:
                Enemy.health -= 10
                print(f"Monster lost 10 health and now has {Enemy.health} health left.\n")
            turns+=1
        elif choice=="B":
            bagChoice=input(f"What would you like to do?\nA. Use a Heal Pot (Qty:{healPots})\nB. Use a Mana Pot (Qty:{manaPots})\nC. Exit bag")
        else:
            print("Not a valid option")

        

    if Player.health<=0:
        print(f"\n\nPlayer lost in {turns} turns.")
    else:
        print(f"\n\nPlayer won in {turns} turns.")
        return Player.health








def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    goblin = Enemy("Goblin", 30, 8, 3)
    orc = Enemy("Orc", 40, 10, 5)

    items = {
        'Sword': {'attack': 5},
        'Shield': {'defense': 3},
    }

# Function to generate a random position for the sword on the grid
def generate_sword_position(grid_size):
    return random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

# Function to generate a random position for the shield on the grid
def generate_shield_position(grid_size):
    return random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

# Function to generate a random position for a goblin on the grid
def generate_goblin_position(grid_size):
    return random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

# Function to check if the player can move in a certain direction
def can_move(x, y, direction, grid_size): # ADD DIAGONALS AND SINGLE LETTER MOVEMENT??
    if direction == 'u':
        return y > 0
    elif direction == 'd':
        return y < grid_size - 1
    elif direction == 'l':
        return x > 0
    elif direction == 'r':
        return x < grid_size - 1
    elif direction =='ur':
        return y > 0 and x < grid_size - 1
    elif direction =='ul':
        return y > 0 and x > 0
    elif direction =='dr':
        return y < grid_size - 1 and x < grid_size - 1
    elif direction =='dl':
        return y < grid_size - 1 and x > 0

# Function to move the player on the grid
def move_player(x, y, direction):
    if direction == 'u':
        return x, y - 1
    elif direction == 'd':
        return x, y + 1
    elif direction == 'l':
        return x - 1, y
    elif direction == 'r':
        return x + 1, y
    elif direction =='ur':
        return x + 1, y - 1
    elif direction =='ul':
        return x - 1, y - 1
    elif direction =='dr':
        return x + 1, y + 1
    elif direction =='dl':
        return x - 1, y + 1

# Size of the grid
grid_size = 10

# Generate random position for the sword
sword_x, sword_y = generate_sword_position(grid_size)

# Generate random position for the shield
shield_x, shield_y = generate_shield_position(grid_size)

# Generate random position for the goblin
goblin_x, goblin_y = generate_goblin_position(grid_size)

# Starting position of the player
player_x, player_y = 0, 0

print(f"The sword is at ({sword_x},{sword_y})")
print(f"The shield is at ({shield_x},{shield_y})")
print(f"The goblin is at ({goblin_x},{goblin_y})")


while True:
    print(f"Player is at position ({player_x}, {player_y})")

    # Check if player is on the sword position
    if (player_x, player_y) == (sword_x, sword_y):
        print("You found the sword!")
        sword_found = True
    elif (player_x, player_y) == (shield_x, shield_y):
        print("You found the shield!")
        shield_found = True   
    elif (player_x, player_y) == (goblin_x, goblin_y):
        print("You found a goblin!")
        combat(Player, Enemy)
    #elif sword_found == True and shield_found == True:
        #break

    # Ask the player for input to choose a direction
    user_direction = input("Enter a direction (u/d/l/r/ur/ul/dr/dl): ").lower()

    # Check if the input direction is valid and the player can move in that direction
    if user_direction in ['u', 'd', 'l', 'r', 'ur', 'ul', 'dr', 'dl'] and can_move(player_x, player_y, user_direction, grid_size):
        player_x, player_y = move_player(player_x, player_y, user_direction)
    else:
        print("Invalid direction or cannot move in that direction. Please try again.")

if __name__ == "__main__":
    main()
