# 02 Number Guessing Game
import random

print("WELCOME TO THE NUMBER GUESSING GAME!")
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
            if player_number > random_number:
                print("Too high.")
                print("Try again!")
                tries += 1
            else:
                print("Too low.")
                print("Try again!")
                tries += 1
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print('You got it!')
    print(f"The number was {random_number}!")
    print(f"You got it in {tries} tries.")
guessing_game()
print(f"Do you want to play again?")
yes_or_no = input("Y/N?: ")
if yes_or_no == "Y":
    guessing_game()
else:
    print("Have a nice day.")