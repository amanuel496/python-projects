from question_model import Question
from data import question_data


def main():
    question_bank = []

    for item in question_data:
        text = item["text"]
        answer = item["answer"]
        question_and_answer = Question(text, answer)
        question_bank.append(question_and_answer)

    print(question_bank[0].text, question_bank[1].answer)


main()
