-- Daunte Robertson ID#620150009

CREATE DATABASE IF NOT EXISTS uwi;

USE uwi;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Address VARCHAR(100),
    Email VARCHAR(100)
);

INSERT INTO Student (StudentID, Name, Address, Email) 
VALUES 
    (62008, 'John Roberts', '10 Holloway Drive', 'jonrrobert@uwi.com'),
    (63009, 'Sally Banner', '5 Main Street', 'sbanner@uwi.com'),
    (64015, 'Bruce Stark', '2 Downing Street', 'bstark@uwi.com'),
    (72001, 'Dianna Banner', '2 Pepsi Ave', 'dbanner@uwi.com'),
    (62909, 'Damon Stark', '1 Dragon Lane', 'dstark@ironthrone.com'),
    (70012, 'Arya Lannister', '2 Hightower Ave', 'alannisterr@starky.com'),
    (40055, 'John Lee', '3 Pepsi Ave', 'jlee@hotmail.com');
    
CREATE TABLE Course (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(100),
    DateCreated DATE
);

INSERT INTO Course (CourseID, CourseName, DateCreated) 
VALUES 
    ('COMP1178', 'Introduction to Python', '2009-10-12'),
    ('BIO8727', 'Exoskeleton', '2010-11-12'),
    ('PHYS1190', 'Quantum Physics', '2009-10-11'),
    ('COMP1190', 'Introduction to C', '2010-11-01'),
    ('COMP1200', 'Introduction to Java', '2012-11-12'),
    ('ECON800', 'Introduction to Statistics', '2015-10-12');
    
CREATE TABLE Enrol (
    StudentID INT,
    CourseID VARCHAR(10),
    Grade INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

INSERT INTO Enrol (StudentID, CourseID, Grade) 
VALUES 
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Python'), 89),
    (62909, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Statistics'), 78),
    (40055, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java'), 48),
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java'), 78),
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Exoskeleton'), 56),
    (72001, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Statistics'), 91),
    (63009, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java'), 67),
    (64015, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Statistics'), 67),
    (70012, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java'), 90),
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Python'), 85),
    (62909, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Python'), 45),
    (63009, (SELECT CourseID FROM Course WHERE CourseName = 'Quantum Physics'), 75),
    (72001, (SELECT CourseID FROM Course WHERE CourseName = 'Quantum Physics'), 69),
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Quantum Physics'), 66),
    (72001, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java'), 70),
    (62008, (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Statistics'), 45);

-- a
SELECT CourseName FROM Course;
-- b
SELECT Name, Address FROM Student;
-- c
SELECT Address FROM Student WHERE Name = 'John Roberts';
-- d
SELECT Name FROM Student WHERE Address LIKE '%Pepsi Ave%';
-- e
SELECT CourseName FROM Course WHERE DateCreated BETWEEN '2009-01-01' AND '2010-12-31';
-- f
SELECT CourseID FROM Course WHERE CourseName = 'Quantum Physics';
-- g
SELECT s.Name
FROM Student s
JOIN Enrol e ON s.StudentID = e.StudentID
WHERE e.CourseID = (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Java');
-- h
SELECT s.Name
FROM Student s
JOIN Enrol e ON s.StudentID = e.StudentID
WHERE e.CourseID = (SELECT CourseID FROM Course WHERE CourseName = 'Introduction to Statistics')
ORDER BY e.Grade DESC
LIMIT 1;
-- i
SELECT c.CourseName, COUNT(*) AS EnrolmentCount
FROM Course c
JOIN Enrol e ON c.CourseID = e.CourseID
GROUP BY c.CourseID
ORDER BY EnrolmentCount DESC
LIMIT 1;
-- j
SELECT c.CourseName, COUNT(*) AS EnrolmentCount
FROM Course c
JOIN Enrol e ON c.CourseID = e.CourseID
GROUP BY c.CourseID
ORDER BY EnrolmentCount ASC
LIMIT 1;
-- k
SELECT c.CourseName
FROM Course c
JOIN Enrol e ON c.CourseID = e.CourseID
ORDER BY e.Grade DESC
LIMIT 1;
-- l 
SELECT s.Name
FROM Student s
JOIN Enrol e ON s.StudentID = e.StudentID
GROUP BY s.StudentID
ORDER BY AVG(e.Grade) DESC
LIMIT 1;
-- m
SELECT AVG(Grade) AS AverageGrade
FROM Enrol
WHERE StudentID = (SELECT StudentID FROM Student WHERE Name = 'John Roberts');
-- n
SELECT s.Name
FROM Student s
JOIN (
    SELECT StudentID
    FROM Enrol
    GROUP BY StudentID
    HAVING COUNT(CourseID) = 6
) AS enrolled_six_courses ON s.StudentID = enrolled_six_courses.StudentID;