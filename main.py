from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from plyer import Player


question_bank = []

for question in question_data:
    question_category = question['category']
    question_difficulty = question['difficulty']
    question_text = question['question']
    question_answer = question['correct_answer']
    detailed_answer = question['detailed_answer']
    new_question = Question(question_difficulty, question_category, question_text, question_answer, detailed_answer)
    question_bank.append(new_question)


player_1 = Player('Третє Око')
player_2 = Player('Виколиглаз')


while True:
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        for _ in range(0, 5):
            quiz.next_question(player_1)

        print('\n--------------------------------------------------------------------------------------------------\n')

        for _ in range(0, 5):
            quiz.next_question(player_2)

        print('\n--------------------------------------------------------------------------------------------------\n')

    print(f'Ви завершили вікторину\n'
          f'--> {player_1.name} має {player_1.get_score()} правильних відповідей з {player_1.get_question_number()}\т'
          f'--> {player_2.name} має {player_2.get_score()} правильних відповідей з {player_2.get_question_number()}')
    break

