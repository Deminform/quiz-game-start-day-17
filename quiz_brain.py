import random
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class QuizBrain:


    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list


    def still_has_questions(self):
        return len(self.question_list) > 0


    def next_question(self):
        random_number = random.randint(0, len(self.question_list) - 1)
        current_question = self.question_list[random_number]
        self.question_list.pop(random_number)
        self.question_number += 1

        question = current_question.text
        category = current_question.category
        difficulty = current_question.difficulty
        correct_answer = current_question.answer

        answer = input(f'Q.{self.question_number} Складність: {difficulty} / Категорія: {category}\nПитання: {question} (Так / Ні?): ')
        self.__check_answer(correct_answer, answer)
        

    def __check_answer(self, correct_answer, user_answer):
        clear()
        if user_answer.lower() == correct_answer.lower():
            print('--> Ти вгадав!')
            self.score += 1
        else:
            print('--> Це неправильно.')
        print(f'Правильна відповідь: {correct_answer}. Твій поточний результат: {self.score}/{self.question_number}.\n')
        
