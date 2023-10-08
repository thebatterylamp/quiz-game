from question_model import Question
from data import question_data_2
from quiz_brain import QuizBrain

question_bank = []

for item in question_data_2:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.has_question():
    quiz.next_ques()

print("You've completed the challenge!")
print(f"Your final score is {quiz.score}/{quiz.q_number} ")
