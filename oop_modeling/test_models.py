import unittest
from models import Person, Student, Teacher
  
class PersonTestCase(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_person_first_name_and_last_name(self):
        first, last = "Ramesh", "Sapkota"
        person = Person(first, last)
        self.assertEqual(person.first_name, first)
        self.assertEqual(person.last_name, last)

    def test_kwargs_params(self):
        first, last = "Ramesh", "Sapkota"
        address, dob, gender = "Kathmandu", "2005-05-03", "female"
        person = Person(first, last, address="Kathmandu", dob=dob, gender=gender)
        self.assertEqual(person.address, address)
        self.assertEqual(person.dob, dob)
        self.assertEqual(person.gender, gender)
  

class TeacherTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_teacher_object_constructor(self):
        teacher = Teacher()
      
    def test_assign_class_teacher(self):
        pass


class StudentTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_teacher_object_constructor(self):
        teacher = Teacher()
      
    def test_assign_class_teacher(self):
        pass


class OurClassTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_our_class_constructor(self):
        pass

        

if __name__ == '__main__': 
    unittest.main() 