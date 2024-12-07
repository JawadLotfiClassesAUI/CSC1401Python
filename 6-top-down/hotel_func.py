from datetime import date
import os

# This version decomposes the program into a main function and other smaller functions
# Top-down design is used to break down the program, so that the overall functionality is easier to understand
# Each function has a single responsibility, making the code easier to read and maintain

def main():
    # Initialize expenses
    roomExpense = 0
    restExpense = 0

    # Display the menu to the user
    displayMenu()
    choice = int(input("choice:"))

    # Loop until the user chooses to quit, calling the corresponding function
    while choice != 5:
        if choice == 1:
            # The handle room expense function returns the updated room expense
            roomExpense = handleRoom(roomExpense)
        elif choice == 2:
            # The handle restaurant expense function returns the updated restaurant expense
            restExpense = handleRest(restExpense)
        elif choice == 3:
            # The store data function only requires the expenses, and doesn't need to return anything
            storeData(roomExpense, restExpense)
        elif choice == 4:
            # The recover data function doesn't require any arguments and doesn't need to return anything
            recoverData()
        else:
            print("Wrong choice")
        
        # Display the menu again for the next choice
        displayMenu()
        choice = int(input("choice:"))

    print("Thank you for using our program")

def displayMenu():
    print('''Choose one of the following options:
    1- Add room expense
    2- Add restaurant expense
    3- Store data in file
    4- Recover data from file
    5- Quit  ''')

def handleRoom(roomExpense):
    expense = float(input("Enter the room expense:"))
    if expense > 0:
        roomExpense += expense
    # Return the updated room expense to the main function
    return roomExpense

def handleRest(restExpense):
    expense = float(input("Enter the restaurant expense:"))
    if expense > 0:
        restExpense += expense
    # Return the updated restaurant expense to the main function
    return restExpense

def storeData(roomExpense, restExpense):
    # Open the file in append mode
    hotelDataFile = open("hotelDataFile.txt", "a")
    # Write the current date and expenses to the file
    hotelDataFile.write(f"{date.today()} {roomExpense} {restExpense}"+'\n')
    # Close the file
    hotelDataFile.close()

def recoverData():
    # Check if the file exists before opening it
    if os.path.exists("hotelDataFile.txt"):
        # Open the file in read mode
        hotelDataFile = open("hotelDataFile.txt", "r")
        # Print the contents of the file
        print(hotelDataFile.read())
        # Close the file
        hotelDataFile.close()
    else:
        # Display file not found message
        print("File not found")

# Call the main function to start the program
main()