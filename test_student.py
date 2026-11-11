import unittest

import student

def setUpModule():
    print("hello this is module level")
    
class TestStudent(unittest.TestCase):
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

    def tearDown(self):
        print("after each test method",self.sid)

if __name__ == "__main__":
    unittest.main()

    