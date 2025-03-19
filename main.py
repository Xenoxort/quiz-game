from question_model import Question

q = 0
score = 0
game_on = True

my_question = Question()

while game_on:
    current_answer, player_answer = my_question.pick_question()
    q += 1

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
        print(f"Your current score is: {score}/{q}")


        if q == 12:
            game_on = False
            print("Game over! Thanks for playing.")





