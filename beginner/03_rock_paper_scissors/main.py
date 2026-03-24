# 03 Rock Paper Scissors
import random

def rock_paper_scissors():
    computer_choice = random.randint(1, 3)
    print('Welcome To Rock Paper Scissors.')
    print('Rock: 1, Paper: 2, Scissors: 3')
    human_choice = None
    while human_choice not in (1, 2, 3):
        try:
            human_choice = int(input('Enter your choice: '))
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue
        
    if human_choice == 1:
        print('Selected Rock!')
        human_choice = "Rock"
    elif human_choice == 2:
        print("Selected Paper!")
        human_choice = "Paper"
    else:
        print("Selected Scissors")
        human_choice = "Scissors"

    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    print(f"Computer's choice: {computer_choice}, Your choice: {human_choice}" )
    
    if computer_choice == "Rock" and human_choice == "Paper":
        print("You win!")
    elif computer_choice == "Paper" and human_choice == "Scissors":
        print("You win!")
    elif computer_choice == "Scissors" and human_choice == "Rock":
        print("You win!")
    elif computer_choice == human_choice:
        print("Its a draw!!")
    else:
        print("You lose!")

rock_paper_scissors()