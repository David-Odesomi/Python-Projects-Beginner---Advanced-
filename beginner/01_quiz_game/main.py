# 01 Quiz Game
import csv

with open("quiz_questions.csv", newline="") as f:
    reader = csv.DictReader(f)
    questions = [row for row in reader]

print("Welcome to Quiz")
print("We have: \n General quiz \n Science Quiz \n History Quiz \n Which one do you want to try out "
      "first?")

quiz_input = input("Quiz: ")
print(quiz_input.title() + " quiz selected.")
