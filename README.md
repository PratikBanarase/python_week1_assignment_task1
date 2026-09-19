# Student Management System

# Project Overview

The Student Management System is a console-based Python application developed as part of the Python Week 1 Assignment.
The application allows users to manage student records through a simple menu-driven interface. It demonstrates Python fundamentals, Object-Oriented Programming (OOP), CRUD operations, input validation, and structured programming.

# Objective

The main objective of this project is to build a practical Python application that demonstrates:
- Python variables and data types
- Conditional statements
- Loops
- Functions and methods
- Classes and objects
- Object-Oriented Programming
- CRUD operations
- User input handling
- Input validation
- Exception handling
- Modular code structure

# Features
The application provides the following features:
1. Add Student
   - Add a new student record.
   - Store student ID, name, age, course, and marks.
2. View Students
   - Display all available student records.
   - Show information in a readable format.
3. Search Student
   - Search for a student using Student ID or Name.
4. Update Student
   - Modify existing student details.
   - Handle invalid student IDs.
5. Delete Student
   - Delete a student record.
   - Ask for confirmation before deletion.
6. Exit
   - Safely exit the application.

# Technologies Used
- Python 3
- Object-Oriented Programming
- Python Lists
- Conditional Statements
- Loops
- Functions
- Exception Handling

# Project Structure

student_management_system/
main.py
models.py
utils.py
README.md

# File Description

File , Description 
`main.py` , Contains the main menu and program flow 
`models.py` , Contains `Student` and `StudentManager` classes 
`utils.py` , Contains utility/validation functions 
`README.md` , Project documentation 

# How to Run

# Step 1: Install Python

Make sure Python 3 is installed on your computer.
Check the version:
python --version

# Step 2: Open the project folder

Open the terminal inside the `student_management_system` folder.

# Step 3: Run the application
python main.py

# Main Menu

===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:

# Sample Input

Enter your choice: 1
Enter student ID: 101
Enter name: Neha
Enter age: 20
Enter course: Python
Enter marks: 91

# Sample Output

Student added successfully.

When viewing students:
===== Student Records =====
ID: 101 | Name: Neha | Age: 20 | Course: Python | Marks: 91

# Search Example

Enter student ID or name: Neha
ID: 101 | Name: Neha | Age: 20 | Course: Python | Marks: 91

# Update Example

Enter student ID to update: 101
Enter new marks: 95
Student updated successfully.

# Delete Example

Enter student ID to delete: 101
Are you sure you want to delete this student? (y/n): y
Student deleted successfully.

# Input Validation

The application validates user input wherever required.
Examples include:
- Invalid menu choices
- Invalid student ID
- Non-numeric age
- Non-numeric marks
- Empty or incorrect input
The program displays user-friendly error messages instead of allowing the application to crash.

# Learning Outcomes

After completing this project, the following concepts are practiced:
- Python syntax
- Control flow
- Functions
- Classes and objects
- Constructors
- Methods
- CRUD operations
- Input validation
- Exception handling
- Modular programming

# Author
Tanvi Bramhankar