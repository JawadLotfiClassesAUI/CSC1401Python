# This file is not a standalone program since it does not make any function calls.
# Instead, it serves as a collection of functions that can be used by other programs.
# By organizing the functions into this custom library, we separate the global logic
# from the detailed implementation, making the project easier to manage and maintain.
from random import randint

# Function to display the difficulty menu
def display_menu():
    print('''
    Choose a difficulty level:
    1 - Beginner (Range: 1 to 100)
    2 - Intermediate (Range: 1 to 1000)
    3 - Hard (Range: 1 to 10000)
    ''')

# Function to choose difficulty level
def choose_difficulty():
    display_menu()
    choice = input("Enter your choice (1/2/3): ")
    while choice != "1" and choice != "2" and choice != "3":
        print("Invalid choice. Please choose 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ")
    return int(choice)

# Function to set the range based on difficulty
def get_range_by_difficulty(difficulty):
    # in Python, we can return multiple values instead of just one
    # base on the difficulty level we return different ranges
    if difficulty == 1:
        return 1, 100
    elif difficulty == 2:
        return 1, 1000
    elif difficulty == 3:
        return 1, 10000

# Function to generate a random secret number
def generate_secret_number(lower, upper):
    return randint(lower, upper)

# Function to handle the game logic and calculate score
def play_game(secret_number, lower, upper, difficulty):
    print(f"Guess the number between {lower} and {upper}.")
    
    # Arbitrarily deciding on a max score based on difficulty
    score = difficulty * 500

    guess = int(input("Your guess: "))
    attempts = 1

    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        guess = int(input("Your guess: "))
        attempts += 1
        # each new guess decreases the score by 50 points
        score -= 50

    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    print(f"You earned {score} points this round!")

    return score

# Function to ask the player if they want to play again
def continuePlaying():
    choice = input("Do you want to play again? (yes/no)").lower()
    while choice != "yes" and choice != "no":
        print("You can only answer with yes or no")
        choice = input("Do you want to play again? (yes/no)")
    if choice == "yes":
        return True
    else:
        return False