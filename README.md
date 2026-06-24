# Student Management System

A simple command-line interface (CLI) application for managing student records. This project was developed as an internship project.

## Features

- Add new student records
- View all student records
- Update existing student records
- Delete student records
- Search for a student by ID
- Data persistence using JSON storage

## Student Information

Each student record contains:
- Student ID
- Name
- Age
- Courses (list of course names)
- Marks (dictionary mapping course names to marks)

## Project Structure

```
student_management_system/
├── src/
│   ├── __init__.py
│   ├── main.py          # Main application entry point
│   ├── student.py       # Student class definition
│   └── storage.py       # JSON storage handling
├── tests/
│   ├── __init__.py
│   └── test_student.py  # Unit tests for Student class
├── .vscode/
│   └── settings.json    # VS Code configuration
├── README.md            # This file
└ requirements.txt
```

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory:
   ```bash
   cd student_management_system
   ```
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies (though this project uses only Python standard library):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the student management system, run:

```bash
python src/main.py
```

You will be presented with a menu of options:
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student by ID
6. Exit

### Running Tests

To run the unit tests:

```bash
python -m unittest discover tests -v
```

### VS Code Setup

If you are using Visual Studio Code, the recommended settings are already provided in `.vscode/settings.json`. Simply open the folder in VS Code and the settings will be applied.

## How It Works

- Student data is stored in a JSON file named `students.json` in the project root directory.
- The application loads existing data from this file on startup and saves changes back to it.
- If the file doesn't exist, it will be created automatically when you add the first student.

## Example Usage

1. Select option 1 to add a new student
2. Enter the requested information (ID, name, age, courses, and marks for each course)
3. Select option 2 to view all students
4. Select option 5 to search for a specific student by ID
5. Select option 3 or 4 to update or delete a student
6. Select option 6 to exit the application

## License

This project is open source and available under the MIT License.

