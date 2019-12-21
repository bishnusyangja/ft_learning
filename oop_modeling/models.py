

class Person:

    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.address = kwargs.get('address' , '')
        self.dob = kwargs.get('dob', None)


class Teachers(Person):
    
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.subject = kwargs.get('subject', '')
        self.is_class_teacher = False

    def assign_class_teacher(self, class_level)
        self.is_class_teacher = True
        self.class_level = class_level


class Students(Person):

    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        subject = kwargs.get('subject', '')
        kwargs.get('is_class_teacher', False)


class OurClass:

    def __init__(self, class_level, year):
        self.class_level = class_level
        self.year = year


class Quitz:

    def __init__(self, *args, **kwargs):
        self.question_list = []

    def set_assigned_by(self, teacher):
        self.assigned_by = teacher

    def set_assigned_to(self, student):
        self.assigned_to = student

    def add_question_list(self, *mcq_list):
        self.question_list.extends(mcq_list)



class MultipleChoiceQuestion:
    
    def __init__(self, *args, **kwargs):
        self.question = args[0]
        self.option_1 = kwargs.get('option_1', '')
        self.option_2 = kwargs.get('option_2', '')
        self.option_3 = kwargs.get('option_3', '')
        self.option_4 = kwargs.get('option_4', '')
        self.right_answer = None

    def set_right_answer(self, answer_number):
        self.right_answer = kwargs.get('right_answer', '') # accepts an option_number

    def get_right_answer(self):
        return f'option_{self.right_answer}'



class QuitzEvaluation:
    
    def __init__(self, student, quitz):
        self.student = student
        self.quitz = quitz
        self.total_answered = 0
        self.grade = None
    
    def assign_grade(self, grade):
        self.grade = grade

    def question_completed(self, answered_now):
        self.total_answered += answered_now


class StudentOverallGrading:

    def __init__(self, student, class_level, **kwargs)
        self.student = student
        self.class_level = class_level
        self.grading = None
        self.year = None

    def set_grading(self, grading, year):
        self.grading = grading
        self.year = year