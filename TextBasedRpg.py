# Imports
import random
import time


# NOTE: MAKE ALL TEXT SLEEPED


# Opening info
time.sleep(0.15)
print("  _____                      _    _____")
time.sleep(0.15)
print(" / ____|                    | |  / ____|")
time.sleep(0.15)
print("| (_____      _____  _ __ __| | | |  __ _   _ _   _")
time.sleep(0.15)
print(" \___ \ \ /\ / / _ \| '__/ _` | | | |_ | | | | | | |")
time.sleep(0.15)
print(" ____) \ V  V / (_) | | | (_| | | |__| | |_| | |_| |")
time.sleep(0.15)
print("|_____/ \_/\_/ \___/|_|  \__,_|  \_____|\__,_|\__, |")
time.sleep(0.15)
print("                                               __/ |")
time.sleep(0.15)
print("                                              |___/ ")
time.sleep(1)
print("\nWelcome to Sword Guy, the turn based adventure RPG where the only limit to power is your patience.\n")

# Variables for when the game ends (not in use)
sword_found=False
shield_found=False
goblin_dead=False
player_dead=False

# Creates class for Player with all stats
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defence = 0

    def display_stats(self):
        print(f"{self.name}'s Stats - \nHealth: {self.health}\n Attack: {self.attack}\n Defence: {self.defence}")

# Creates class for Enemy with all stats        
class Enemy:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def display_stats(self):
        print(f"{self.name}'s Stats - \nHealth: {self.health}\n Attack: {self.attack}\n Defence: {self.defence}")

# Combat variables
turns=0
healPots=3
manaPots=3

# Code for combat when encountering goblin
def combat(player, goblin):
    global turns, healPots, manaPots, player_dead, goblin_dead
    
    while player.health > 0 and goblin.health> 0:
        diceRollArray = []
        
        for i in range(5):
            diceRollArray.append(random.randint(1, 6))

        choice=input("Do you want to: A. take your turn, or B. use an item? ").upper()
        if choice=="A":
            total = sum(diceRollArray)
            print(f"Turn {turns+1}")
            print(f"You rolled {diceRollArray} and got a total of {total}.")
            
            if total < 20:
                player.health -= 10
                print(f"You lost 10 health and now has {player.health} health left.\n")
            else:
                goblin.health -= 10
                print(f"Monster lost 10 health and now has {goblin.health} health left.\n")
            turns+=1
        elif choice=="B":
            bagChoice=input(f"What would you like to do?\nA. Use a Heal Potion (Qty:{healPots})\nB. Use a Mana Potion (Qty:{manaPots})\nC. Exit bag\n").upper()
            if bagChoice=="A":
                healPots-=1
                player.health+=30
                if player.health>=100:
                    player.health=100
                print(f"Heal potion used.\nYou now have {healPots} Heal Potions left.\nYou are now on {player.health} health.")
        else:
            print("Not a valid option")

    if player.health<=0:
        print(f"You lost in {turns} turns.\n")
        player_dead=True
    else:
        print(f"You won in {turns} turns.\n")
        goblin_dead=True
        return player.health

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
def can_move(x, y, direction, grid_size):
    if direction == 'w':
        return y > 0
    elif direction == 's':
        return y < grid_size - 1
    elif direction == 'a':
        return x > 0
    elif direction == 'd':
        return x < grid_size - 1
    elif direction =='wd':
        return y > 0 and x < grid_size - 1
    elif direction =='wa':
        return y > 0 and x > 0
    elif direction =='sd':
        return y < grid_size - 1 and x < grid_size - 1
    elif direction =='sa':
        return y < grid_size - 1 and x > 0

# Function to move the player on the grid
def move_player(x, y, direction):
    if direction == 'w':
        return x, y - 1
    elif direction == 's':
        return x, y + 1
    elif direction == 'a':
        return x - 1, y
    elif direction == 'd':
        return x + 1, y
    elif direction =='wd':
        return x + 1, y - 1
    elif direction =='wa':
        return x - 1, y - 1
    elif direction =='sd':
        return x + 1, y + 1
    elif direction =='sa':
        return x - 1, y + 1

# Size of the grid
grid_size = 10

# Function for general usage code
def main():
    global sword_found, shield_found, goblin_dead, player_dead
    time.sleep(1)
    player_name = input("Enter your character's name: ").title()
    player = Player(player_name)

    goblin = Enemy("Goblin", 30, 8, 3)
    orc = Enemy("Orc", 40, 10, 5)

    items = {
        'Sword': {'attack': 5},
        'Shield': {'defence': 3},
    }

    # Generate random position for the sword # NOTE: Make not able to spawn in same place
    sword_x, sword_y = generate_sword_position(grid_size)

    # Generate random position for the shield
    shield_x, shield_y = generate_shield_position(grid_size)

    # Generate random position for the goblin
    goblin_x, goblin_y = generate_goblin_position(grid_size)

    # Starting position of the player
    player_x, player_y = 0, 0

    #Prints general info
    print("\n0,0 is the top left corner\n")

    # Prints item positions for testing
    print(f"The sword is at ({sword_x},{sword_y})\n")
    print(f"The shield is at ({shield_x},{shield_y})\n")
    print(f"The goblin is at ({goblin_x},{goblin_y})\n")

    # Prints player position
    while True:
        print(f"{player_name} is at position ({player_x}, {player_y})\n") # NOTE: Make random when bigger and more items

        # Check if player is on the sword position
        if (player_x, player_y) == (sword_x, sword_y):
            print("You found the sword!\n")
            player.attack+=3
            print(f"{player_name}'s damage now increased to {player.attack}.")
            sword_found = True
        elif (player_x, player_y) == (shield_x, shield_y):
            print("You found the shield!\n")
            player.health+=10
            player.defence+=1
            print(f"{player_name}'s health now increased to {player.health}.")
            print(f"{player_name}'s defence now increased to {player.defence}.")
            shield_found = True   
        elif (player_x, player_y) == (goblin_x, goblin_y):
            print("You found a goblin!\n")
            combat(player, goblin)
        if player_dead == True:
            quit()
        elif goblin_dead == True and sword_found == True and shield_found == True:
            print("Congraulations! You win!")
            quit()

        # Ask the player for input to choose a direction
        user_direction = input("Enter a direction (w for up/s for down/a for left/d for right/wd for up & right/wa for up & left/sd for down & right/sa for down & left): ").lower()

        # Check if the input direction is valid and the player can move in that direction
        if user_direction in ['w', 's', 'a', 'd', 'wd', 'wa', 'sd', 'sa'] and can_move(player_x, player_y, user_direction, grid_size):
            player_x, player_y = move_player(player_x, player_y, user_direction)
        else:
            print("Invalid direction or cannot move in that direction. Please try again.")

if __name__ == "__main__":
    main()
