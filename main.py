from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_category = question['category']
    question_difficulty = question['difficulty']
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_difficulty, question_category, question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f'Ви завершили вікторину\nВаш підсумковий бал склав {quiz.score} / {quiz.question_number}')