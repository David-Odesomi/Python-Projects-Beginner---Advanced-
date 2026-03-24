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
    elif human_choice == 2:
        print("Selected Paper!")
    else:
        print("Selected Scissors")

    print(f"Computer's choice: {computer_choice}, Your choice: {human_choice}" )
    
    if computer_choice == 1 and human_choice == 2:
        print("You win!")
    elif computer_choice == 2 and human_choice == 3:
        print("You win!")
    elif computer_choice == 3 and human_choice == 1:
        print("You win!")
    elif computer_choice == human_choice:
        print("Its a draw!!")
    else:
        print("You lose!")

rock_paper_scissors()