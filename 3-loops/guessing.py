from random import randint

answer = "yes"
while answer == "yes":

    goal = randint(0, 100)
    score = 1000

    print("""This game has 2 difficulty options:
        1 : easy
        2 : hard""")
    difficulty = int(input("Enter your choice:"))
    while difficulty != 1 and difficulty != 2:
        difficulty = int(input("You have to choose 1 or 2:"))

    guess = int(input("Enter your guess:"))
    attempts = 1
    while True:
        if guess == goal:
            print("Congratulations, you found the hidden number")
            print(f"Your score is {score}")
            break
        elif attempts >= 5 and difficulty == 2:
            print("You have lost")
            break
        elif guess > goal:
            print("Try a lower value")
        elif guess < goal:
            print("Try a higher value")
        guess = int(input("Enter your guess:"))
        attempts += 1
        score -= 100
    # after a break execution resumes here
    answer = input("Do you want to continue? (yes/no)")
print("Thank you for playing the game, see you next time")