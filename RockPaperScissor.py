import random

def get_user_choice():
    while True:
        user_choice = input(" Welcome to Rock paper Scissor Game \n Choose  any one i.e rock or  paper or scissors:").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid Choice please enter the input as above mentioned")
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    user_score = 0
    computer_score = 0
    while True:
        print("\nLet's play Rock-Paper-Scissors!")
        user_choice = get_user_choice()
        computer_choice = computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"\nYour score: {user_score}, Computer's score: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing.See you soon !")
            break
if __name__ == "__main__":
     main()
