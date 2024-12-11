#!/usr/bin/env python3 

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# print(question_bank[0].text, question_bank[0].answer) # sanity check

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question() 

print('You\'ve complated the quiz!')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')