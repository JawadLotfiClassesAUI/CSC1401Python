# This file is not a standalone program since it does not make any function calls.
# Instead, it serves as a collection of functions that can be used by other programs.
# By organizing the functions into this custom library, we separate the global logic
# from the detailed implementation, making the project easier to manage and maintain.

from datetime import date
import os

# Function to display the menu options to the user
def displayMenu():
    print('''Choose one of the following options:
    1- Add room expense
    2- Add restaurant expense
    3- Store data in file
    4- Recover data from file
    5- Quit  ''')

# Function to handle room-related expenses
def handleRoom(roomExpense):
    expense = float(input("Enter the room expense:"))
    if expense > 0:
        roomExpense += expense
    return roomExpense

# Function to handle restaurant-related expenses
def handleRest(restExpense):
    expense = float(input("Enter the restaurant expense:"))
    if expense > 0:
        restExpense += expense
    return restExpense

# Function to store the current data into a file
def storeData(roomExpense, restExpense):
    hotelDataFile = open("hotelDataFile.txt", "a")
    hotelDataFile.write(f"{date.today()} {roomExpense} {restExpense}"+'\n')
    hotelDataFile.close()

# Function to recover previously stored data from a file
def recoverData():
    if os.path.exists("hotelDataFile.txt"):
        hotelDataFile = open("hotelDataFile.txt", "r")
        print(hotelDataFile.read())
        hotelDataFile.close()
    else:
        print("File not found.")