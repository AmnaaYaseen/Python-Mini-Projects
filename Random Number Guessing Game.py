from random import*
print("Welcome to Random Number Guessing Game")
while True:
    num_of_guess = 1
    num_guess_by_comp = randint(1, 100)
    num_guess_by_user = int(input('Guess the number between 1 and 100: '))
    while num_guess_by_user != num_guess_by_comp:
        if num_guess_by_user > num_guess_by_comp:
            print('Too high, try again')
        else:
            print('Too low, try again')
        num_guess_by_user = int(input("Try again: "))
        num_of_guess += 1
    print('Congratulations, you guessed the right number')
    print('Number of Guesses: ', num_of_guess)
    play_or_not = input('If you want to play again type Yes otherwise '
                        'type No: ').strip().lower()
    if play_or_not == "no":
        print("Thanks for playing...GoodBye!")
        break

