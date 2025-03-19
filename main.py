import random
from data import question_data

remaining_questions = question_data.copy()
n_questions = len(question_data)

now = 1
game_on = True

while game_on:
    current_data = random.choice(remaining_questions)
    current_question = current_data["text"]
    current_answer = current_data["answer"]

    question = input(f"Q.{now}: {current_question} (True/False)?: ").lower()

    if question == "off":
        game_on = False

    remaining_questions.remove(current_data)
    now += 1
    print(len(remaining_questions))





