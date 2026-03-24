# 02 Number Guessing Game
import random



def guessing_game():
    random_number = random.randint(1, 10)
    player_number = input("Enter in your guess: ")

    while player_number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,):
        try:
            print("Enter a valid Number Bro: ")
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

    if player_number == random_number:
        print("You guessed correctly.")
    elif player_number - 1 or player_number + 1 == random_number:
        print("So close.")
    else:
        print("You didnt get it.")