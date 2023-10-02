# Task 4
# Rock-Paper-Scissors Game
import random
print("Welcome to Rock, Paper, Scissors!")
user_score = 0
computer_score = 0

while True:
    user_selection = input('\nChoose 1.Rock 2.Paper 3.Scissors: ')
    options = 'Rock', 'Paper', 'Scissors'
    computer_selection = random.choice(options)
    print(computer_selection)
    if ((user_selection == "rock" or user_selection == "Rock") and computer_selection == "Scissors") or ((user_selection == "scissors" or user_selection == "Scissors") and computer_selection == "Paper") or ((user_selection == "paper" or user_selection == "Paper") and computer_selection == "Rock"):
        result = "You win!"
    elif (user_selection == computer_selection) or (user_selection == "rock" and computer_selection == "Rock") or (user_selection == "paper" and computer_selection == "Paper") or (user_selection == "scissors" and computer_selection == "Scissors"):
        result = "It's a tie!"
    else:
        result = "You lose!"
    print(f'{result}\n')

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    elif result == "It's a tie!":
        user_score += 0
        computer_score += 0
    print("Your score:", user_score)
    print("Computer's score:", computer_score)

    play_again = input("Do you want to play again? (Yes or No):")
    if play_again == "No" or play_again == "no":
        break
if user_score > computer_score:
    print("\nFinal Result: You win!")
elif user_score < computer_score:
    print("\nFinal Result: You Lose!")
else:
    print("\nFinal Result: It's a tie!")


