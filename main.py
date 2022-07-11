from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from user_interface import QuizInterface

question_list = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
quiz_interface = QuizInterface(quiz)
