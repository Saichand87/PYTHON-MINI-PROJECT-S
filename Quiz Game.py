# Quiz Game in Python

def display_question(question, options):
    print(question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if answer in [1, 2, 3, 4]:
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 4
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
            "answer": 3
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Pb", "Fe"],
            "answer": 1
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": 3
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["0", "1", "2", "-1"],
            "answer": 3
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1905", "1898", "1920"],
            "answer": 1
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Quartz"],
            "answer": 3
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Helium", "Hydrogen", "Lithium", "Oxygen"],
            "answer": 2
        }
    ]

    score = 0

    for q in questions:
        display_question(q["question"], q["options"])
        user_answer = get_user_answer()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q["options"][q["answer"] - 1]
            print(f"Wrong! The correct answer was: {correct_option}\n")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
