# 01 Quiz Game
import csv
import pandas as pd

df = pd.read_csv('quiz_questions.csv')
print(df)
print(df.columns)
print(df.shape)

category = input('What subject do you want to do?')
filtered = df[df['category'] == category]
print(filtered) 

shuffled = filtered.sample(n=5)
shuffled = shuffled.reset_index(drop=True)

score = 0

for i, row in shuffled.interrows():
    print(f"\nQ{i + 1}: {row['question']}")
    print(f" A) {row['option_a']}")
    print(f" B) {row['option_b']}")
    print(f" C) {row['option_c']}")
    print(f" D) {row['option_d']}")

answer =input('Your answer? (A/B/C/D): ').strip().upper()

if answer == row['answer']:
    print('correct')
    score += 1

else: 
    print(f'Wrong. Answer was {row['answer']}')

print(f"\nQuiz done! You scored {score}/{len(shuffled)}")