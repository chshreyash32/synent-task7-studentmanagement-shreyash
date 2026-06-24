class Student:
    def __init__(self, student_id, name, age, courses, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = courses  # List of course names
        self.marks = marks      # Dictionary of course: marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "courses": self.courses,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            courses=data["courses"],
            marks=data["marks"]
        )

    def average_marks(self):
        """Calculate the average marks across all courses."""
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Courses: {self.courses}, Marks: {self.marks}"
