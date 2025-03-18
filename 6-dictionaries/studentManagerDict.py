from studentUtilsDict import *

def main():
    # Initialize an empty list to store student data as dictionaries
    listOfStudents = []
    
    # Display the menu to the user
    printMenu()
    choice = input("Enter your choice: ")

    # Loop until the user chooses to quit
    while choice != '4':
        # Call the appropriate function based on the user's choice
        if choice == '1':
            add_student(listOfStudents)
        elif choice == '2':
            view_students(listOfStudents)
        elif choice == '3':
            delete_student(listOfStudents)
        elif choice == '5':
            display_statistics(listOfStudents)
        else:
            print("Invalid choice. Please try again.")
        
        # Display the menu again for the next iteration
        printMenu()
        choice = input("Enter your choice: ")

# The main function is called here to start the program
main()
