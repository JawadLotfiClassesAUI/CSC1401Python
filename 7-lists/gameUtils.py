#### Level 1 functions
def initialize_grid(numOfRows, numOfColumns):
    grid = []
    for row in range(numOfRows):
        # Add an empty list for each row
        grid.append([])
        # Loop through each column in the current row
        for column in range(numOfColumns):
            # Add a space character to represent an empty cell
            grid[row].append(" ")
    return grid

def play_game(grid, numOfRows, numOfColumns):
    empty_cells = numOfRows * numOfColumns

    while empty_cells > 0:
        play_turn(grid, 'X')
        print_grid(grid, numOfRows, numOfColumns)
        empty_cells -= 1
        if check_winner(grid, numOfRows, numOfColumns, 'X'):
            print("Player X wins!")
            return
        if empty_cells == 0:
            break

        play_turn(grid, 'O')
        print_grid(grid, numOfRows, numOfColumns)
        empty_cells -= 1
        if check_winner(grid, numOfRows, numOfColumns, 'O'):
            print("Player O wins!")
            return

#### Level 2 functions
def play_turn(grid, player_char):
    row = int(input(f"Enter the row for {player_char} : ")) - 1
    column = int(input(f"Enter the column for {player_char} : ")) - 1
    while grid[row][column] != " ":
        print("Cell is already occupied. Try again.")
        row = int(input(f"Enter the row for {player_char} : ")) - 1
        column = int(input(f"Enter the column for {player_char} : ")) - 1
    grid[row][column] = player_char

def print_grid(grid, numOfRows, numOfColumns):
    # Print the top border of the grid
    print_top_border(numOfColumns)
    for row in range(numOfRows):
        # Print the left border of the grid
        print("│", end="")
        for column in range(numOfColumns):
            # Print the cell value followed by a separator
            print(f"{grid[row][column]}", end="│")
        print()
        # Print the row separator or bottom border
        if row == numOfRows - 1:
            print_bottom_border(numOfColumns)
        else:
            print_row_separator(numOfColumns)

def check_winner(grid, numOfRows, numOfColumns, player_char):
    if check_rows(grid, numOfRows, player_char):
        return True
    if check_columns(grid, numOfColumns, player_char):
        return True
    if check_diagonals(grid, numOfRows, numOfColumns, player_char):
        return True
    return False

#### Level 3 functions

# Helper functions for printing the grid
def print_top_border(numOfColumns):
    verticalBars = numOfColumns - 1
    print("┌" + "─" * (numOfColumns + verticalBars)  + "┐")

def print_row_separator(numOfColumns):
    verticalBars = numOfColumns - 1
    print("├" + "─" * (numOfColumns + verticalBars) + "┤")

def print_bottom_border(numOfColumns):
    verticalBars = numOfColumns - 1
    print("└" + "─" * (numOfColumns + verticalBars) + "┘")


# Helper functions for checking the winner
def check_rows(grid, numOfRows, player_char):
    for row in range(numOfRows):
        row_winner = True  # Initialize flag variable
        for cell in grid[row]:
            if cell != player_char:
                row_winner = False  # Update flag if cell does not match player_char
                break  # Exit inner loop early if row is not a winning row
        if row_winner:
            return True  # Return early if a winning row is found
    return False  # Return False if no winning row is found

def check_columns(grid, numOfColumns, player_char):
    for column in range(numOfColumns):
        column_winner = True
        for row in grid:
            if row[column] != player_char:
                column_winner = False
                break
        if column_winner:
            return True
    return False

def check_diagonals(grid, numOfRows, numOfColumns, player_char):
    diagonal_winner = True
    for i in range(min(numOfRows, numOfColumns)):
        if grid[i][i] != player_char:
            diagonal_winner = False
            break
    if diagonal_winner:
        return True

    diagonal_winner = True
    for i in range(min(numOfRows, numOfColumns)):
        if grid[i][numOfColumns - i - 1] != player_char:
            diagonal_winner = False
            break
    if diagonal_winner:
        return True

    return False