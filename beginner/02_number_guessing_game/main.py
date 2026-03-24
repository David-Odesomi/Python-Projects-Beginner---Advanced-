# 02 Number Guessing Game
import random



def guessing_game():
    random_number = random.randint(1, 10)
    player_number = None

    while player_number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,):
        try:
            player_number = int(input("Enter in your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

    if player_number == random_number:
        print("You guessed correctly.")
    elif player_number - 1 == random_number or player_number + 1 == random_number:
        print("So close.")
    else:
        print("You didnt get it.")

guessing_game()