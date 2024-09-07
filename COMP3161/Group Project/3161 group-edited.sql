DROP DATABASE IF EXISTS course_management;
CREATE DATABASE course_management;
USE course_management;

-- Core Tables

CREATE TABLE User_Account (
  user_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  username VARCHAR(50) UNIQUE NOT NULL,
  user_password VARCHAR(100) NOT NULL, 
  account_type VARCHAR(20) CHECK(account_type IN ('admin', 'lecturer', 'student'))
);

CREATE TABLE Admin (
  admin_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER UNIQUE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User_Account(user_id)
);

CREATE TABLE Student (
  student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER UNIQUE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User_Account(user_id)
);

CREATE TABLE Lecturer (
  lecturer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER UNIQUE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User_Account(user_id)
);

CREATE TABLE Course (
  course_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  lecturer_id INTEGER, 
  course_name VARCHAR(100) NOT NULL,
  description TEXT,
  FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id)
);

CREATE TABLE Course_Content (
  content_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  course_id INTEGER NOT NULL, 
  content_title VARCHAR(100),
  file_path VARCHAR(255),
  content_type VARCHAR(50), 
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Discussion_Forum (
  forum_id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Changed course_id to forum_id
  course_id INTEGER NOT NULL,
  forum_name VARCHAR(100),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Discussion_Thread (
  thread_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  forum_id INTEGER NOT NULL, -- Changed course_id to forum_id
  thread_title VARCHAR(100) NOT NULL,
  thread_content TEXT,
  FOREIGN KEY (forum_id) REFERENCES Discussion_Forum(forum_id)
);

CREATE TABLE Calendar_Event (
  event_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  course_id INTEGER, 
  event_description TEXT,
  event_title VARCHAR(100),
  assignment_due_date DATE, 
  FOREIGN KEY (course_id) REFERENCES Course(course_id) 
);

CREATE TABLE Section (
  section_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  course_id INTEGER NOT NULL, 
  section_title VARCHAR(100),
  lecture_slides VARCHAR(255),
  links VARCHAR(255),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Section_Item (
  item_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  section_id INTEGER NOT NULL,
  item_title VARCHAR(100),
  item_content TEXT,
  FOREIGN KEY (course_id) REFERENCES Course(course_id),
  FOREIGN KEY (section_id) REFERENCES Section(section_id)
);

CREATE TABLE Assignment (
  assignment_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  course_id INTEGER NOT NULL, 
  student_id INTEGER NOT NULL,
  assignment_title VARCHAR(100),
  grade FLOAT,
  FOREIGN KEY (course_id) REFERENCES Course(course_id), 
  FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- ... rest of the tables and views



CREATE TABLE CreateAccount (
    admin_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    creation_date DATE NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES Admin(admin_id),
    FOREIGN KEY (user_id) REFERENCES User_Account(user_id)
);

-- Relational Tables

CREATE TABLE Schedule (
    lecturer_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    date DATE NOT NULL, 
    PRIMARY KEY (lecturer_id, event_id), 
    FOREIGN KEY (lecturer_id) REFERENCES Lecturer(lecturer_id),
    FOREIGN KEY (event_id) REFERENCES Calendar_Event(event_id)
);

CREATE TABLE ReplyTo (
    thread_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    reply TEXT,
    PRIMARY KEY(thread_id, student_id), 
    FOREIGN KEY (thread_id) REFERENCES Discussion_Thread(thread_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

CREATE TABLE AssignedTo (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    average FLOAT, 
    PRIMARY KEY (student_id, course_id), 
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE VIEW courses_with_50_plus_students AS
SELECT c.course_id, c.course_name, COUNT(*) AS student_count
FROM AssignedTo a
INNER JOIN Course c ON a.course_id = c.course_id
GROUP BY c.course_id
HAVING COUNT(*) >= 50;

CREATE VIEW students_with_5_plus_courses AS
SELECT student_id, COUNT(*) AS course_count
FROM AssignedTo
GROUP BY student_id
HAVING COUNT(*) >= 5;


-- View 3: Lecturers teaching 3 or more courses
CREATE VIEW lecturers_with_3_plus_courses AS
SELECT lecturer_id, COUNT(*) as course_count
FROM Course
GROUP BY lecturer_id
HAVING COUNT(*) >= 3;


-- View 4: Top 10 courses by enrollment
CREATE VIEW top_10_enrolled_courses AS
SELECT c.course_id, c.course_name, COUNT(*) AS student_count
FROM AssignedTo a
INNER JOIN Course c ON a.course_id = c.course_id
GROUP BY c.course_id
ORDER BY student_count DESC
LIMIT 10;

-- View 5: Top 10 students by overall average grade
CREATE VIEW top_10_students_by_average AS
SELECT student_id, AVG(average) AS overall_average
FROM AssignedTo a
INNER JOIN Course c ON a.course_id = c.course_id
WHERE average IS NOT NULL
GROUP BY student_id
ORDER BY overall_average DESC
LIMIT 10;

