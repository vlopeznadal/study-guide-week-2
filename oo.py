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

class StudentExam():
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print(f'Score: {self.score:.2f}')

def example():

    exam = Exam('Final')

    question_1 = Question(
        "What is the parent class for a non-inheriting Python class?", "object"
    )
    exam.add_question(question_1)

    question_2 = Question(
        "Which special method determines how to initialize instances?",
        "__init__",
    )
    exam.add_question(question_2)

    student = Student("Virginia", "Lopez Nadal", "0101 Computer Street")

    virginia_exam = StudentExam(student, exam)
    virginia_exam.take_test()

