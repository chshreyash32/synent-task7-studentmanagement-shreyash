import json
import os

DATA_FILE = "students.json"

def load_students():
    """Load students from JSON file. Returns a list of Student objects."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Student.from_dict(student_data) for student_data in data]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading data: {e}")
        return []

def save_students(students):
    """Save list of Student objects to JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump([student.to_dict() for student in students], f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

# Import Student class to avoid circular imports
from .student import Student
