# This program counts down seconds from a user input to 0
from time import sleep  # Import the sleep function from the time library to pause execution

start = int(input("Enter the start value:"))

# The range function takes three parameters: start, stop, and step.
# start: the starting value of the sequence
# stop: the end value of the sequence (exclusive), set to -1 to include 0 in the countdown
# step: the amount by which the value is decremented, set to -1 to count downwards
for counter in range(start, -1, -1):
    print(counter)
    sleep(1)  # Pause execution for 1 second