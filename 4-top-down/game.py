from gameUtils import *

# Main function that handles the game
def main():
    # Top-level function that provides the overall structure of the game
    print("Welcome to the Number Guessing Game!")
    total_score = 0
    playAgain = True

    while playAgain:
        # High-level function call to choose the difficulty of the game
        difficulty = choose_difficulty()
        # Function call to get the range of numbers based on the chosen difficulty
        lower, upper = get_range_by_difficulty(difficulty)
        # Function call to generate the secret number within the specified range
        secret_number = generate_secret_number(lower, upper)

        # Function call to play the game and return the score for the current round
        score = play_game(secret_number, lower, upper, difficulty)
        
        total_score += score
        print(f"Your current total score is: {total_score}")
        
        # Function call to check if the player wants to continue playing
        playAgain = continuePlaying()

# Start the game
main()