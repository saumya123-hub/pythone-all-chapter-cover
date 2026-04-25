import random
choices = ["rock","paper","scissors"]
while True:
    user = input("Choose rock, paper , or scissors:").lower()
    computer = random.choice(choices)
    print("computer chose:",computer)
    if user == computer:
        print("it is a tie!")
    else(user == "rock" and computer == "scissors") or \
    (user == "scissors" and computer == "paper"):
        print("you win!")
else:
    print("you lose!")
play_again = input("play again" (yes/no))