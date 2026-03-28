# 02 Number Guessing Game
import random

def guessing_game():
    tries = 0
    while True:
        try:
            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))
            if number1 > 20 or number2 > 20:
                print("Your numbers must be between 0-20, try again.")
            elif number1 >= number2:
                print("First number must be less than the second, try again.")
            else:
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

    random_number = random.randint(number1, number2)
    player_number = None

    while player_number != random_number:
        try:
            player_number = int(input("Enter your guess: "))
            if player_number + 1 == random_number or player_number - 1 == random_number:
                print("So close!")
            else:
                print("Try again!")
                tries += 1
            if player_number > random_number:
                print("Too high. Try lower.")
            else:
                print("Too low. Try higher.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print('You got it!')
    print(f"The number was {random_number}!")
    print(f"You got it in {tries} tries.")

guessing_game()