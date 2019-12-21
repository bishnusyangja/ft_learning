

class Person:
    '''
    This class holds first_name, last_name, address, dob, gender of the person.
    '''

    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.address = kwargs.get('address' , '')
        self.dob = kwargs.get('dob', None)
        self.gender = kwargs.get('gender', '')


class Teachers(Person):
    '''
    This class holds the information of a teacher
    all params of Person with subject that he teaches and is_class_teacher
    '''
    
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.subject = kwargs.get('subject', '')
        self.is_class_teacher = False
        self.is_principal = False

    def assign_class_teacher(self, class_level)
        self.is_class_teacher = True
        self.class_level = class_level

    def set_principal_of_school():
        self.is_principal = True


class Students(Person):
    '''
    This class holds the information of a student with base class Person
    It also holds the roll no of a student
    '''

    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.roll_no = kwargs.get('roll_no', '')


class OurClass:
    '''
    This class holds the information of number of class for e.g class_number 7 means, it is 7 class.
    And year indicates that all the student information, quitz and grade of students are relating to year of class (e.g. 7 class of 2019) 
    '''

    def __init__(self, class_number, year):
        self.class_number = class_number
        self.year = year


class Quitz:
    '''
    This class holds the all question_list for a subject and a class, questions can be added partially and student can also answer the
    question of a quitz set partially.
    '''

    def __init__(self, subject, class_level, **kwargs):
        self.subject = subject,
        self.class_level = class_level # (here class_level holds the object of OurClass)
        self.question_list = []

    def set_assigned_by(self, teacher):
        self.assigned_by = teacher

    def set_assigned_to(self, student):
        self.assigned_to = student

    def add_question_list(self, *mcq_list):
        self.question_list.extends(mcq_list)



class MultipleChoiceQuestion:
    
    def __init__(self, ques, **kwargs):
        self.question = ques
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
    '''
    This class is for overall grading of a student for a year in one class.
    For example, John in 2019 is in class 8 and his overall grading is A+ for all of the quitz in all subjects.
    In this case, object of this class holds params:
    student (John: Student object), 
    class_level (8 : OurClass Object, contains 2019 year within this object)
    '''

    def __init__(self, student, class_level, **kwargs)
        self.student = student
        self.class_level = class_level  # (Object of OurClass)
        self.grading = None

    def set_grading(self, grading):
        self.grading = grading