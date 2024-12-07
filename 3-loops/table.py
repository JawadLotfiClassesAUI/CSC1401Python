# Get the number of rows and columns from the user
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

# Outer loop to iterate over each row
for row in range(1, num_rows + 1):
    # Inner loop to iterate over each column in the current row
    for column in range(1, num_columns + 1):
        # Print the product of the current row and column, formatted to align properly
        print(f"{column*row:>4}", end="")
    # Print a newline character after each row to move to the next line
    print("")