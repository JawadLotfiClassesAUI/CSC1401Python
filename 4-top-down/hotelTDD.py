# Importing all functions from the custom library 'hotelUtils'
# This helps in separating the global logic from the detailed implementation
from hotelUtils import *

def main():
    roomExpense = 0
    restExpense = 0

    # Display the menu to the user
    displayMenu()
    choice = int(input("choice:"))

    while choice != 5:
        if choice == 1:
            # Calling external function to handle room-related expenses
            roomExpense = handleRoom(roomExpense)
        elif choice == 2:
            # Calling external function to handle restaurant-related expenses
            restExpense = handleRest(restExpense)
        elif choice == 3:
            # Calling external function to store the current data
            storeData(roomExpense, restExpense)
        elif choice == 4:
            # Calling external function to recover previously stored data
            recoverData()
        else:
            print("Wrong choice")
        
        # Display the menu again for the next operation
        displayMenu()
        choice = int(input("choice:"))

    print("Thank you for using our program")

# Entry point of the program
main()