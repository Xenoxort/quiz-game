from question_model import Question
from quiz_brain import Quiz

my_question = Question()
my_quiz = Quiz()

game_on = my_quiz.game_on

while game_on:
    #Handle question
    current_answer, player_answer, question_number = my_question.pick_question()

    #Quit game if answer is off
    game_on = my_quiz.game_off(player_answer)

    #Evaluate answer
    if game_on:
        my_quiz.answer(player_answer, current_answer, question_number)

    #End game if no question left
    if question_number == 12:
        game_on = False
        print("Game over! Thanks for playing.")





