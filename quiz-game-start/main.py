from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for item in question_data:
        question = item["question"]
        correct_answer = item["correct_answer"]
        question_and_answer = Question(question, correct_answer)
        question_bank.append(question_and_answer)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


main()
