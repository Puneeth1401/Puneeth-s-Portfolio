import random

# Define the board layout
board = {
    1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99,
    32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78
}

# Define the dice simulator function
def roll_dice():
    return random.randint(1, 6)

# Define the main game function
def play_game():
    # Initialize player position
    player_position = 0

    # Game loop
    while True:
        # Roll the dice
        input("Press Enter to roll the dice...")
        steps = roll_dice()
        print(f"You rolled a {steps}!")

        # Move the player
        player_position += steps
        if player_position > 100:
            player_position = 100

        if player_position in board:
            # Move up or down the ladder or snake
            if player_position < board[player_position]:
                print(f"You climbed a ladder from {player_position} to {board[player_position]}!")
            else:
                print(f"You slid down a snake from {player_position} to {board[player_position]}.")

            # Move to the new position
            player_position = board[player_position]

        # Check for win
        if player_position == 100:
            print("Congratulations! You won!")
            break

        # Print current position
        print(f"You are now at position {player_position}.\n")

# Start the game
print("Welcome to Snake and Ladder!")
play_game()