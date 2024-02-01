import random

# NOTE: Fix issue where all preivously travelled tiles become a 1 when moved off of

# World positioning
def print_world(world, player_row, player_column):
    for i, row in enumerate(world): # Allows you to keep track of the number of loops or things
        for j, cell in enumerate(row):
            if i == player_row and j == player_column:
                print("8", end=" ")  # Print the player position
            elif (abs(i - player_row) <= 2 and abs(j - player_column) <= 2 and world[i][j] == 0): # Absolute value
                print("W", end=" ")  # Print "W" for river within 2 spaces
            else:
                print(world[i][j], end=" ")
        print()

# Movement
def move_player(world, current_row, current_column, previous_value):
  while True:
        move = input("Enter a direction (up/down/left/right): ").lower()

        new_row, new_column = current_row, current_column  # Initialize with current position
        if move == "up" and current_row > 0:
            new_row -= 1
        elif move == "down" and current_row < len(world) - 1:
            new_row += 1
        elif move == "left" and current_column > 0:
            new_column -= 1
        elif move == "right" and current_column < len(world[0]) - 1:
            new_column += 1
        else:
            print("Invalid direction. Please try again.")  # Inform the user of invalid input
            continue  # Restart the loop to prompt for a valid input

        if world[new_row][new_column] == 0:
            print("You cannot move into the river. Please try again.")
        else:
            # Update the current position with the previous value
            world[current_row][current_column] = previous_value
            # Update the new cell with the player value
            world[new_row][new_column] = 8
            return new_row, new_column, world[current_row][current_column]




# World as an array
worldData=[
    [2,2,2,2,2,2,1,1,1,1,0,1,1],
    [2,2,4,4,2,2,1,1,1,0,1,1,1],
    [2,4,4,2,2,1,1,1,1,5,1,1,1],
    [2,2,2,2,1,1,1,1,1,0,1,1,1],
    [2,3,2,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,4,4,1,1,1,1,1,1,0,1,1,1],
    [1,4,4,1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,4,4,4,0,1,1,1,1],
    [1,1,1,1,4,4,4,5,1,1,1,1,1],
    [1,1,1,1,4,4,0,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,4,1]
    ]

# NOTE: 0 is river 1 is land 2 is mountain 3 is entrance 4 is house 5 is bridge 8 is player




num_rows = len(worldData)
num_columns = len(worldData[0]) if num_rows > 0 else 0

while True:
    player_row = random.randint(0, num_rows - 1)
    player_column = random.randint(0, num_columns - 1)
    player_starting_pos = worldData[player_row][player_column]

    if player_starting_pos != 0:
        break

worldData[player_row][player_column] = 8

# Main loop for player movement
player_previous_value = player_starting_pos  # This line tracks the cell's original value
while True:
    # Check for nearby river within 2 spaces
    if any(worldData[i][j] == 0 for i in range(max(0, player_row - 2), min(num_rows, player_row + 3)) for j in range(max(0, player_column - 2), min(num_columns, player_column + 3))):
        print("You can hear flowing water")

    if any(
        worldData[i][j] == 4 for i in range(max(0, player_row - 2), min(num_rows, player_row + 3)) for j in range(max(0, player_column - 2), min(num_columns, player_column + 3))):
        print("You can hear talking nearby")
    
    # Move the player and print the world
    print("\n\n")  # You can use "\n" for new lines to clean up code
    print_world(worldData, player_row, player_column)
    # Here we pass player_previous_value to move_player to 'leave behind' as we move to a new cell
    player_row, player_column, player_previous_value = move_player(worldData, player_row, player_column, player_previous_value)
