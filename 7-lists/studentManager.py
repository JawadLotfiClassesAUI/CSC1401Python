from studentUtils import *

def main():
    # Initialize empty lists to store student data
    ids = []
    names = []
    gpas = []

    # Display the menu to the user
    printMenu()
    choice = input("Enter your choice: ")

    # Loop until the user chooses to quit
    while choice != '4':
        # Call the appropriate function based on the user's choice
        if choice == '1':
            add_student(ids, names, gpas)
        elif choice == '2':
            view_students(ids, names, gpas)
        elif choice == '3':
            delete_student(ids, names, gpas)
        elif choice == '5':
            display_statistics(gpas)
        else:
            print("Invalid choice. Please try again.")
        
        # Display the menu again for the next iteration
        printMenu()
        choice = input("Enter your choice: ")

# The main function is called here to start the program
# Note how the main function is simple and easy to understand
# It only shows the high-level algorithm and delegates the complexities
# to the functions defined in the utils library
main()