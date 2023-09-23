import random


def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Rock, Paper, Scissors!")
    username = input("Enter your username: ")
    print(f"Hello, {username}!")
    
    user_score = 0
    computer_score = 0
    winning_score = 3
    
    while user_score < winning_score and computer_score < winning_score:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"{username} chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Score - {username}: {user_score} | Computer: {computer_score}")
    
    if user_score >= winning_score:
        print(f"Congrats, {username}! You won! {user_score}-{computer_score}.")
    else:
        print(f"Computer wins! {computer_score}-{user_score}.")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
