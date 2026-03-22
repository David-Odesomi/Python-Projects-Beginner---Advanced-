import pandas as pd

df = pd.read_csv('quiz_questions.csv')

category = input('What subject do you want to do? (General/Science/History): ').strip().title()
filtered = df[df['category'] == category]

if filtered.empty:
    print(f"No questions found for '{category}'. Try General, Science, or History.")
else:
    shuffled = filtered.sample(n=5).reset_index(drop=True)
    score = 0

    for i, row in shuffled.iterrows():
        print(f"\nQ{i + 1}: {row['question']}")
        print(f"  A) {row['option_a']}")
        print(f"  B) {row['option_b']}")
        print(f"  C) {row['option_c']}")
        print(f"  D) {row['option_d']}")

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == row['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Answer was {row['answer']}")

    print(f"\nQuiz done! You scored {score}/5")