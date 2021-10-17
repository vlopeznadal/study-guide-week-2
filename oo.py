class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = input(self.question + " > ")
        return self.correct_answer == answer

class Exam(object):
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        answer_tally = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                answer_tally += 1
                
        return 100 * (float(answer_tally) / len(self.questions))
