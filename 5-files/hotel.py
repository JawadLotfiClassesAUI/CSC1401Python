from datetime import date
import os

# Initialize room and restaurant expenses to 0
roomExpense = 0
restExpense = 0

# Start an infinite loop to display the menu and process user choices
while True:
    # Display the menu options
    print('''Choose one of the following options:
    1- Add room expense
    2- Add restaurant expense
    3- Store data in file
    4- Recover data from file
    5- Quit  ''')
    
    # Get the user's choice
    choice = int(input("choice:"))

    # If the user chooses to add room expense
    if choice == 1:
        # Get the room expense amount from the user
        expense = float(input("Enter the room expense:"))
        # Add the expense to the total if it's positive
        if expense > 0:
            roomExpense += expense
    
    # If the user chooses to add restaurant expense
    elif choice == 2:
        # Get the restaurant expense amount from the user
        expense = float(input("Enter the restaurant expense:"))
        # Add the expense to the total if it's positive
        if expense > 0:
            restExpense += expense
    
    # If the user chooses to store data in a file
    elif choice == 3:
        # Open the file in append mode
        hotelDataFile = open("hotelDataFile.txt", "a")
        # Write the current date and expenses to the file
        hotelDataFile.write(f"{date.today()} {roomExpense} {restExpense}"+'\n')
        # Close the file
        hotelDataFile.close()
    
    # If the user chooses to recover data from the file
    elif choice == 4:
        # Check if the file exists before opening
        if os.path.exists("hotelDataFile.txt"):
            # Open the file in read mode
            hotelDataFile = open("hotelDataFile.txt", "r")
            # Print the contents of the file
            print(hotelDataFile.read())
            # Close the file
            hotelDataFile.close()
        else:
            # Print a file not found message
            print("File not found.")
    
    # If the user chooses to quit
    elif choice == 5:
        # Print a thank you message and break the loop
        print("Thank you for using our program")
        break
    
    # If the user enters an incorrect choice
    else:
        # Print an error message
        print("You have entered an incorrect choice")