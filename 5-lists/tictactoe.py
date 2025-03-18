from gameUtils import *

def main():
    # Get the number of rows and columns from the user
    numOfRows = int(input("number of rows:"))
    numOfColumns = int(input("number of columns:"))
    
    # Initialize the grid with the specified number of rows and columns
    grid = initialize_grid(numOfRows, numOfColumns)
    
    # Starts the game
    play_game(grid, numOfRows, numOfColumns)

main()