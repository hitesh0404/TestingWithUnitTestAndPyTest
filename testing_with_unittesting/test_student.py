import unittest
import platform
import unittesting.student as student
from unittest.mock import Mock

def setUpModule():
    print("hello this is module level")
    
class TestStudent(unittest.TestCase):

    @unittest.skipIf(platform.system()=="Darwin","not for mac")
    def test_not_for_mac(self):
        self.assertIsInstance(student.Student(1,"hp",11),object)

    def test_student_random_password(self):
        student.random.randint = Mock()
        student.random.randint.return_value = 1
        hp = student.Student(1,"hp",22)
        self.assertEqual(hp.get_password(),5253)


    def test_student_random_password(self):
            student.random.randint = Mock()
            student.random.randint.return_value = 1
            hp = student.Student(1,"hp",22)
            self.assertEqual(hp.get_password(),5253)

    @classmethod
    def setUpClass(cls):
        print("this is class level")

    def setUp(self):
        print("before each test method")
        self.sid = student.Student(1,"Sid",22)

    def test_student_id(self):
        self.assertEqual(1,self.sid.id,"id is 2")

    def test_student_name(self):
        # sid = student.Student(1,"Sid",22)
        assert "Sid" == self.sid.name

    def test_student_age(self):
        # sid = student.Student(1,"Sid",22)
        assert 22 == self.sid.age

    def test_student_negative_age(self):
        with self.assertRaises(student.AgeException) :
            student.Student(1,"Sid",-22)


    def tearDown(self):
        print("after each test method",self.sid)

if __name__ == "__main__":
    unittest.main()

    