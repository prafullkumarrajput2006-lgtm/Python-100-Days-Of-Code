# Excercise 3...Question...




# Create a program capable of displaying questions to the user like KBC... 




questions = [
    {
        "question": "What is the Capital of U.P.?",
        "options": ["A. Mumbai", "B. Rajasthan", "C. Lucknow", "D. Bihar"],
        "answer": "C",
        "prize": 10000
    },

    {
        "question": "What is the national animal of India?",
        "options": ["A. Tiger", "B. Cow", "C. Dog", "D. Cat"],
        "answer": "A",
        "prize": 20000
    },

    {
        "question": "Who is the Prime Minister of India?",
        "options": ["A. Modi", "B. Rahul", "C. Shah", "D. None of these"],
        "answer": "A",
        "prize": 30000
    },

    {
        "question": "What is the duration of our National Anthem?",
        "options": ["A. 45 Sec", "B. 50 Sec", "C. 52 Sec", "D. 55 Sec"],
        "answer": "C",
        "prize": 50000
    }
]

total_prize = 0

print("===== Welcome to KBC =====")

for q in questions:

    print("\nQuestion:", q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid Answer!")
        break

    if user_answer == q["answer"]:
        total_prize = q["prize"]

        print("Correct Answer!")
        print("You won Rs.", total_prize)

    else:
        print("Wrong Answer!")
        print("Correct answer was:", q["answer"])
        break

else:
    print("\nCongratulations! You completed all questions.")

print("\nYour total prize money is Rs.", total_prize)
print("===== THANK YOU FOR PLAYING =====")

