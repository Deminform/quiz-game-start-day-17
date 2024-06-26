import random
from plyer import Player
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        self.question_count = len(self.question_list)

    def still_has_questions(self):
        return len(self.question_list) > 0

    def next_question(self, player: Player):
        random_number = random.randint(0, len(self.question_list) - 1)
        current_question = self.question_list[random_number]
        self.question_list.pop(random_number)
        player.set_question_number()
        self.question_count -= 1
        question = current_question.text
        category = current_question.category
        difficulty = current_question.difficulty
        correct_answer = current_question.answer
        detailed_answer = current_question.detailed_answer

        answer = input(
            f'player --> {player.name} <-- \nQ.{player.get_question_number()} Складність: {difficulty} / Категорія: '
            f'{category}\nПитання: {question} (Так / Ні?): ')
        self.__check_answer(correct_answer, answer, player, detailed_answer)

    def __check_answer(self, correct_answer, user_answer, player: Player, detailed_answer):
        clear()
        if user_answer.lower() == correct_answer.lower():
            print('--> Ти вгадав!')
            player.set_score()
        else:
            print('--> Це неправильно.')
        print(f'Правильна відповідь: {detailed_answer}.\nТвій поточний результат: '
              f'{player.get_score()}/{player.get_question_number()}.\n'
              f'Питаннь залишилось: {self.question_count}\n\n')
