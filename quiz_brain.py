class Quiz:
    def __init__(self):
        self.score = 0
        self.game_on = True


    def game_off(self, player_answer):
        if player_answer == "off":
            self.game_on = False
            print("Game over! Thanks for playing.")
        return self.game_on

    def answer(self, player_answer, current_answer, question_number):
        if player_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {current_answer}.")
        print(f"Your current score is: {self.score}/{question_number}")



