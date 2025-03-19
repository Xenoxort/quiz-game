from data import question_data
import random

class Question:
    def __init__(self):
        self.now = 0
        self.remaining_questions = question_data.copy()

    def pick_question(self):
        self.now += 1
        current_data = random.choice(self.remaining_questions)
        current_question = current_data["text"]
        current_answer = current_data["answer"]

        player_answer = input(f"Q.{self.now}: {current_question} (True/False)?: ")
        self.remaining_questions.remove(current_data)

        return current_answer, player_answer


