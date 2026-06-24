import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("S001", "John Doe", 20, ["Math", "Science"], {"Math": 90, "Science": 85})
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.courses, ["Math", "Science"])
        self.assertEqual(student.marks, {"Math": 90, "Science": 85})
    
    def test_average_marks(self):
        student = Student("S001", "John Doe", 20, ["Math", "Science"], {"Math": 90, "Science": 90})
        self.assertEqual(student.average_marks(), 90.0)
        
        student2 = Student("S002", "Jane Doe", 22, ["English"], {"English": 80})
        self.assertEqual(student2.average_marks(), 80.0)
        
        student3 = Student("S003", "Bob", 21, [], {})
        self.assertEqual(student3.average_marks(), 0.0)
    
    def test_to_dict(self):
        student = Student("S001", "John Doe", 20, ["Math"], {"Math": 90})
        expected = {
            "student_id": "S001",
            "name": "John Doe",
            "age": 20,
            "courses": ["Math"],
            "marks": {"Math": 90}
        }
        self.assertEqual(student.to_dict(), expected)
    
    def test_from_dict(self):
        data = {
            "student_id": "S001",
            "name": "John Doe",
            "age": 20,
            "courses": ["Math"],
            "marks": {"Math": 90}
        }
        student = Student.from_dict(data)
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.courses, ["Math"])
        self.assertEqual(student.marks, {"Math": 90})

if __name__ == '__main__':
    unittest.main()
