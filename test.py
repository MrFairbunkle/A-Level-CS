import random

def print_world(world, player_row, player_column):
    for i, row in enumerate(world):
        for j, cell in enumerate(row):
            if i == player_row and j == player_column:
                print("8", end=" ")  # Print the player position
            elif (
                abs(i - player_row) <= 2
                and abs(j - player_column) <= 2
                and world[i][j] == 0
            ):
                print("W", end=" ")  # Print "W" for river within 2 spaces
            else:
                print(world[i][j], end=" ")
        print()

def move_player(world, current_row, current_column, previous_value):
    # Update the current position with the previous value
    world[current_row][current_column] = previous_value

    move = input("Enter a direction (up/down/left/right): ").lower()

    if move == "up" and current_row > 0:
        current_row -= 1
    elif move == "down" and current_row < len(world) - 1:
        current_row += 1
    elif move == "left" and current_column > 0:
        current_column -= 1
    elif move == "right" and current_column < len(world[0]) - 1:
        current_column += 1

    # Get the initial value of the cell where the player is moving to
    initial_value = world[current_row][current_column]

    # Update the new cell with the player value
    world[current_row][current_column] = 8

    return current_row, current_column, initial_value





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

# NOTE: 0 is river 1 is land 2 is mountain 3 is entrance 4 is house 5 is bridge 8 is




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
while True:
    # Check for nearby river within 2 spaces
    if any(
        worldData[i][j] == 0
        for i in range(max(0, player_row - 2), min(len(worldData), player_row + 3))
        for j in range(max(0, player_column - 2), min(len(worldData[0]), player_column + 3))
    ):
        print("You can hear flowing water")

    # Move the player and print the world
    print("")
    print("")
    print_world(worldData, player_row, player_column)
    player_row, player_column, previous_value = move_player(worldData, player_row, player_column, worldData[player_row][player_column])