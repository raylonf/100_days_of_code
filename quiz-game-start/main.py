from question_model import QuizGameModel
from data import question_data2
from quiz_brain import QuizBrain

game =  QuizGameModel(question_data2)
jogo = QuizBrain()
jogo.game(game)

