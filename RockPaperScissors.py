import random
while True:
    user_action = input("Enter a choice(Rock, Paper, or Scissors):")

    possible_actions = ["Rock", "Paper", "Scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper cover rock! You win!")
        else:
            print("Scissor cuts paper! You lose.")
    elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissor cuts paper! You lose!")
            else:
                print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n)")
    if play_again != "y":
      break