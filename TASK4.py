import random

#user's choice
def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

#computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == "rock" and computer_choice == "scissors") or
          (user_choice == "scissors" and computer_choice == "paper") or
          (user_choice == "paper" and computer_choice == "rock")):
        return "You win!"
    else:
        return "Computer wins!"

#play the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Main game loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
