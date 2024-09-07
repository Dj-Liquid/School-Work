-- Daunte Robertson ID#620150009

CREATE DATABASE IF NOT EXISTS uwiV2;

USE uwiV2;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    CourseCode VARCHAR(10)
);

CREATE TABLE Lecturers (
    LecId INT PRIMARY KEY,
    LecName VARCHAR(100),
    Department VARCHAR(100)
);

CREATE TABLE Teaches (
    LecId INT,
    CourseID INT,
    PRIMARY KEY (LecId, CourseID),
    FOREIGN KEY (LecId) REFERENCES Lecturers(LecId),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Grades (
    Grade INT,
    CourseID INT,
    StudentID INT,
    PRIMARY KEY (Grade, CourseID, StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

SELECT LecName, COUNT(*) AS NumCoursesTaught
FROM Teaches
JOIN Lecturers ON Teaches.LecId = Lecturers.LecId
GROUP BY LecName
ORDER BY NumCoursesTaught DESC
LIMIT 1;

SELECT LecName, COUNT(*) AS NumCoursesTaught
FROM Teaches
JOIN Lecturers ON Teaches.LecId = Lecturers.LecId
GROUP BY LecName
ORDER BY NumCoursesTaught ASC
LIMIT 1;

SELECT CourseName, COUNT(*) AS NumStudents
FROM Grades
JOIN Courses ON Grades.CourseID = Courses.CourseID
GROUP BY CourseName;

SELECT CourseName, AVG(Grade) AS AvgGrade
FROM Grades
JOIN Courses ON Grades.CourseID = Courses.CourseID
GROUP BY CourseName;

SELECT StudentID, AVG(Grade) AS AvgGrade
FROM Grades
GROUP BY StudentID
ORDER BY AvgGrade DESC
LIMIT 1;

SELECT StudentID, AvgGrade
FROM (
    SELECT StudentID, AVG(Grade) AS AvgGrade
    FROM Grades
    GROUP BY StudentID
    ORDER BY AvgGrade DESC
    LIMIT 10
) AS TopTenSmartest
ORDER BY AvgGrade ASC;
