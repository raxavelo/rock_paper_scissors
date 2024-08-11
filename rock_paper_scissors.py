import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_choice == "q":
        break

    if user_choice not in options:
        print("Invalid choice. Please choose Rock/Paper/Scissors.")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print(f"Computer picked {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        continue
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_wins += 1
        print("You win!")
    else:
        computer_wins += 1
        print("Computer wins!")

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
