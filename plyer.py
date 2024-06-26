class Player:
    def __init__(self, name):
        self.score = 0
        self.question_number = 0
        self.name = name

    def set_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def set_question_number(self):
        self.question_number += 1

    def get_question_number(self):
        return self.question_number
