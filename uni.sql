CREATE TABLE IF NOT EXISTS Departments (
    
DepartmentID INTEGER  ,
    DepartmentName VARCHAR(100) NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    DOB DATE NOT NULL,
    Address VARCHAR(255),
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) UNIQUE NOT NULL,
    DepartmentName VARCHAR(100),
    FOREIGN KEY (DepartmentName) REFERENCES Departments(DepartmentName)
);

CREATE TABLE IF NOT EXISTS Courses (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseName VARCHAR(100) NOT NULL  ,
    Credits INT NOT NULL,
    DepartmentName VARCHAR(100),
    FOREIGN KEY (DepartmentName) REFERENCES Departments(DepartmentName)
);

CREATE TABLE IF NOT EXISTS Faculty (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(100),
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) UNIQUE NOT NULL,
    DepartmentName VARCHAR(100),
    FOREIGN KEY (DepartmentName) REFERENCES Departments(DepartmentName)
);

CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    CourseID INTEGER,
    EnrollmentDate DATE NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE IF NOT EXISTS Grades (
    GradeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EnrollmentID INTEGER UNIQUE,
    Grade CHAR(1),
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID)
);

CREATE TABLE IF NOT EXISTS Schedules (
    ScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseID INTEGER,
    FacultyID INTEGER,
    Day VARCHAR(20) NOT NULL,
    Time TIME NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);
