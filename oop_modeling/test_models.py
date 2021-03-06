import unittest
from models import Person, Student, Teacher, OurClass, Quitz, MultipleChoiceQuestion, QuitzEvaluation, \
    StudentOverallGrading


# I am familiar with unit-test, functional-test and end to end test using selenium in python. Here I am
# writing just unit test only.
class PersonTestCase(unittest.TestCase): 

    def test_person_first_name_and_last_name(self):
        first, last = "Ramesh", "Sapkota"
        person = Person(first, last)
        self.assertEqual(person.first_name, first)
        self.assertEqual(person.last_name, last)

    def test_kwargs_params(self):
        first, last = "Ramesh", "Sapkota"
        address, dob, gender = "Kathmandu", "2005-05-03", "female"
        person = Person(first, last, address=address, dob=dob, gender=gender)
        self.assertEqual(person.address, address)
        self.assertEqual(person.dob, dob)
        self.assertEqual(person.gender, gender)
  

class TeacherTestCase(unittest.TestCase):

    def test_teacher_object_constructor(self):
        first_name, last_name, subject = 'Ram', 'Dai', 'Science'
        teacher = Teacher(first_name, last_name, subject=subject)
        self.assertEqual(teacher.first_name, first_name)
        self.assertEqual(teacher.last_name, last_name)
        self.assertEqual(teacher.subject, subject)
        self.assertFalse(teacher.is_class_teacher)
        self.assertFalse(teacher.is_principal)

    def test_assign_class_teacher(self):
        first_name, last_name, subject = 'Ram', 'Dai', 'Science'
        class_level = OurClass(6, 2018)
        teacher = Teacher(first_name, last_name, subject=subject)
        teacher.assign_class_teacher(class_level)
        self.assertTrue(teacher.is_class_teacher)
        self.assertEqual(teacher.class_level, class_level)

    def test_set_principal_of_school(self):
        first_name, last_name, subject = 'Ram', 'Dai', 'Science'
        teacher = Teacher(first_name, last_name, subject=subject)
        teacher.set_principal_of_school()
        self.assertTrue(teacher.is_principal)


class StudentTestCase(unittest.TestCase):

    def test_teacher_object_constructor(self):
        first_name, last_name, roll_no = 'Babu', 'Aryal', 567
        student = Student(first_name, last_name, roll_no=roll_no)
        self.assertEqual(student.first_name, first_name)
        self.assertEqual(student.last_name, last_name)
        self.assertEqual(student.roll_no, roll_no)


class OurClassTestCase(unittest.TestCase):

    def test_our_class_constructor(self):
        class_number, year = 5, 2020
        obj = OurClass(class_number, year)
        self.assertEqual(obj.class_number, class_number)
        self.assertEqual(obj.year, year)


class QuitzTestCase(unittest.TestCase):

    def test_quitz_constructor(self):
        subject, class_level = 'English', OurClass(7, 2015)
        quitz = Quitz(subject, class_level)
        self.assertEqual(quitz.subject, subject)
        self.assertEqual(quitz.class_level, class_level)
        self.assertEqual(len(quitz.question_list), 0)

    def test_set_assigned_by(self):
        subject, class_level = 'English', OurClass(7, 2015)
        first_name, last_name, subject = 'Ram', 'Dai', 'Science'
        teacher = Teacher(first_name, last_name, subject=subject)
        quitz = Quitz(subject, class_level)
        quitz.set_assigned_by(teacher)
        self.assertEqual(quitz.assigned_by, teacher)

    def test_assigned_to(self):
        subject, class_level = 'English', OurClass(7, 2015)
        first_name, last_name, roll_no = 'Babu', 'Aryal', 567
        student = Student(first_name, last_name, roll_no=roll_no)
        quitz = Quitz(subject, class_level)
        quitz.set_assigned_to(student)
        self.assertEqual(quitz.assigned_to, student)

    def test_add_question_list(self):
        subject, class_level = 'English', OurClass(7, 2015)
        mcq_list = [MultipleChoiceQuestion('What is your name ?'),
            MultipleChoiceQuestion('What is your age ?')
         ]
        quitz = Quitz(subject, class_level)
        quitz.add_question_list(mcq_list)
        self.assertEqual(len(quitz.question_list), len(mcq_list))


class MultipleChoiceQuestionTestCase(unittest.TestCase):

    def test_multiple_choice_question_constructor(self):
        ques = 'What is your name ?'
        mcq = MultipleChoiceQuestion(ques, option_1='a', option_2='b',
                                     option_3='c', option_4='d')
        self.assertEqual(mcq.question, ques)

    def test_set_right_answer(self):
        ques = 'What is your name ?'
        mcq = MultipleChoiceQuestion(ques, option_1='a', option_2='b',
                                     option_3='c', option_4='d')
        mcq.set_right_answer(1)
        self.assertEqual(mcq.right_answer, 1)

    def test_get_right_answer(self):
        ques = 'What is your name ?'
        mcq = MultipleChoiceQuestion(ques, option_1='a', option_2='b',
                                     option_3='c', option_4='d')
        mcq.set_right_answer(1)
        self.assertEqual(mcq.get_right_answer(), 'a')


class QuitzEvaluationTestCase(unittest.TestCase):

    def test_quitz_evaluation_constructor(self):
        subject, class_level = 'English', OurClass(7, 2015)
        quitz = Quitz(subject, class_level)
        first_name, last_name, roll_no = 'Babu', 'Aryal', 567
        student = Student(first_name, last_name, roll_no=roll_no)
        evaluation = QuitzEvaluation(student, quitz)
        self.assertEqual(evaluation.student, student)
        self.assertEqual(evaluation.quitz, quitz)
        self.assertIsNone(evaluation.grade)
        self.assertEqual(evaluation.total_answered, 0)


class StudentOverallGradingTestCase(unittest.TestCase):

    def test_overall_grading_constructor(self):
        first_name, last_name, roll_no = 'Babu', 'Aryal', 567
        student, class_level = Student(first_name, last_name, roll_no=roll_no), OurClass(7, 2015)
        overall_grading = StudentOverallGrading(student, class_level)
        self.assertEqual(overall_grading.student, student)
        self.assertEqual(overall_grading.class_level, class_level)
        self.assertIsNone(overall_grading.grading)

    def test_set_grading(self):
        first_name, last_name, roll_no = 'Babu', 'Aryal', 567
        student, class_level = Student(first_name, last_name, roll_no=roll_no), OurClass(7, 2015)
        overall_grading = StudentOverallGrading(student, class_level)
        grading = 'A+'
        overall_grading.set_grading(grading)
        self.assertEqual(overall_grading.grading, grading)


if __name__ == '__main__': 
    unittest.main() 