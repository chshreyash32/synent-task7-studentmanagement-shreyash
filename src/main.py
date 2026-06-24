import sys
from .student import Student
from .storage import load_students, save_students

def add_student(students):
    """Add a new student."""
    print("\n--- Add New Student ---")
    try:
        student_id = input("Enter Student ID: ").strip()
        # Check if ID already exists
        if any(s.student_id == student_id for s in students):
            print("Error: Student ID already exists.")
            return
        
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        courses = []
        marks = {}
        
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            course = input(f"Enter course {i+1} name: ").strip()
            mark = int(input(f"Enter mark for {course}: "))
            courses.append(course)
            marks[course] = mark
        
        student = Student(student_id, name, age, courses, marks)
        students.append(student)
        save_students(students)
        print("Student added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_students(students):
    """Display all students."""
    print("\n--- All Students ---")
    if not students:
        print("No students found.")
        return
    
    for student in students:
        print(student)

def update_student(students):
    """Update an existing student."""
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to update: ").strip()
    student = next((s for s in students if s.student_id == student_id), None)
    
    if not student:
        print("Student not found.")
        return
    
    print(f"Current details: {student}")
    print("Leave blank to keep current value.")
    
    try:
        name = input(f"Enter new name (current: {student.name}): ").strip()
        if name:
            student.name = name
        
        age_input = input(f"Enter new age (current: {student.age}): ").strip()
        if age_input:
            student.age = int(age_input)
        
        # Update courses and marks
        print("\nCurrent courses and marks:")
        for course in student.courses:
            print(f"  {course}: {student.marks[course]}")
        
        update_courses = input("\nUpdate courses and marks? (y/n): ").lower()
        if update_courses == 'y':
            courses = []
            marks = {}
            num_courses = int(input("Enter number of courses: "))
            for i in range(num_courses):
                course = input(f"Enter course {i+1} name: ").strip()
                mark = int(input(f"Enter mark for {course}: "))
                courses.append(course)
                marks[course] = mark
            student.courses = courses
            student.marks = marks
        
        save_students(students)
        print("Student updated successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_student(students):
    """Delete a student."""
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()
    student = next((s for s in students if s.student_id == student_id), None)
    
    if not student:
        print("Student not found.")
        return
    
    confirm = input(f"Are you sure you want to delete student {student.name} (ID: {student.student_id})? (y/n): ").lower()
    if confirm == 'y':
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

def search_student(students):
    """Search for a student by ID."""
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ").strip()
    student = next((s for s in students if s.student_id == student_id), None)
    
    if student:
        print(f"\nStudent found:\n{student}")
    else:
        print("Student not found.")

def display_menu():
    """Display the main menu."""
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student by ID")
    print("6. Exit")
    print("=================================")

def main():
    """Main function to run the student management system."""
    students = load_students()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
