from data import question_data
from QuestionModel import Question
from QuizBrainModel import QuizBrain

import os
clear = lambda: os.system("cls")
clear()

print("Welcome to quiz: \n")

question_data_resutls = question_data["results"]
question_bank = []
for question in question_data_resutls:
    QuestionObj = Question(question["question"], question["correct_answer"])
    question_bank.append(QuestionObj)

QuizBrainObj = QuizBrain(question_bank)

while QuizBrainObj.is_questions_left():
    QuizBrainObj.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {QuizBrainObj.score}/{QuizBrainObj.quesiton_number}")