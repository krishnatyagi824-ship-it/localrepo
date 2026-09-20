import random

# Snake and Ladder positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 99}

def roll_dice():
    return random.randint(1, 6)

def play_game():
    position = 0
    while position < 100:
        input("Press Enter to roll the dice...")
        dice = roll_dice()
        print(f"You rolled a {dice}")
        position += dice

        if position > 100:
            position -= dice  # don't move if overshoot
            print("You need exact number to win!")
            continue

        # Snake check
        if position in snakes:
            print("hiss that might have hurted")
            position = snakes[position]

        # Ladder check
        elif position in ladders:
            print("yeye you climbed on to something")
            position = ladders[position]

        print(f"You are now at position {position}")

        # Winning condition
        if position == 100:
            print("Nice luck to be won")
            break

# Run the game
play_game()
