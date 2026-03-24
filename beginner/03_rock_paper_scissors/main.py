# 03 Rock Paper Scissors
import random

computer_choice = random.randint(1,3)

def rock_paper_scissors():
    computer_choice = random.randint(1, 3)
    print('Welcome To Rock Paper Scissors.')
    print('Rock: 1, Paper: 2, Scissors: 3')
    human_choice = int(input('Enter your choice: '))
    while human_choice != 1 or 2 or 3:
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
    

rock_paper_scissors()