# 02 Number Guessing Game
import random



def guessing_game():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    player_number = None

    while player_number != random_number:
        try:
            player_number = int(input("Enter in your guess: "))
            if player_number + 1 == random_number or player_number - 1 == random_number:
                print("So close.")
            else: 
                print("Try again!")
        except ValueError:
            print("⚠️  Please enter a valid number.\n")

            continue
    print('You got it!')
    print(f"The number was {random_number}!")
        

guessing_game()