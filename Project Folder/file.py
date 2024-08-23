import random

print("Welcome to App - Rocks, Paper, Scissors ")

user_won = 0
computer_won = 0

options = ["rocks", "paper", "scissors"]

while True:
    user_pick = input("Select rocks/paper/scissors or q to quit: ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick, ".")

    if user_pick == "rocks" and computer_pick == "scissors":
        user_won += 1
        print("You won!")
    elif user_pick == "scissors" and computer_pick == "paper":
        user_won += 1
        print("You won!")
    elif user_pick == "paper" and computer_pick == "rocks":
        user_won += 1
        print("You won!")
    else:
        computer_won += 1
        print("Computer won!")

print("You won", user_won, "times")
print("Computer won", computer_won, "times")
