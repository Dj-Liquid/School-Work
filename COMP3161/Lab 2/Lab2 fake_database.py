from faker import Faker
import random

fake = Faker()

students = [(i, fake.first_name(), fake.last_name()) for i in range(1, 201)]

# Generate 10 lecturers
lecturers = [(i, fake.name(), fake.job()) for i in range(1, 11)]

# Generate 50 courses
courses = [(i, fake.catch_phrase(), fake.random_int(1000, 9999)) for i in range(1, 51)]

# Generate course-lecturer assignments
teaches = [(random.choice(lecturers)[0], course_id) for course_id in range(1, 51)]

# Generate grades for students in courses
grades = []

# Randomly assign students to courses
for course_id in range(1, 51):
    # Randomly select a subset of students for each course
    students_in_course = random.sample(range(1, 201), random.randint(1, 20))
    # Generate grades for selected students in the course
    for student_id in students_in_course:
        grade = random.randint(50, 100)
        grades.append((grade, course_id, student_id))

with open('insert_queries.sql', 'w') as f:
    for student in students:
        f.write(f"INSERT INTO Students (StudentID, FirstName, LastName) VALUES {student};\n")
    for lecturer in lecturers:
        f.write(f"INSERT INTO Lecturers (LecId, LecName, Department) VALUES {lecturer};\n")
    for course in courses:
        f.write(f"INSERT INTO Courses (CourseID, CourseName, CourseCode) VALUES {course};\n")
    for teach in teaches:
        f.write(f"INSERT INTO Teaches (LecId, CourseID) VALUES {teach};\n")
    for grade in grades:
        f.write(f"INSERT INTO Grades (Grade, CourseID, StudentID) VALUES {grade};\n")