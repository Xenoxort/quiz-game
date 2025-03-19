import random
import data

remaining_questions = data.question_data.copy()
n_questions = len(data.question_data)

now = 0
score = 0
game_on = True

while game_on:
    now += 1
    current_data = random.choice(remaining_questions)
    current_question = current_data["text"]
    current_answer = current_data["answer"]

    player_answer = input(f"Q.{now}: {current_question} (True/False)?: ")

    if player_answer == "off":
        game_on = False
        print("Game over! Thanks for playing.")

    else:
        if player_answer.lower() == current_answer.lower():
            print("You got it right!")
            score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {current_answer}.")
        print(f"Your current score is: {score}/{now}")

        remaining_questions.remove(current_data)

        if len(remaining_questions) == 0:
            game_on = False
            print("Game over! Thanks for playing.")
        #print(len(remaining_questions))





