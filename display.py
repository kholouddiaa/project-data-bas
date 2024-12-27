from connection import execute_query
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk


def display_students_view():
    def fetch_students():
        query = "SELECT * FROM Students"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Students")

    columns = ("StudentID", "Name", "DOB", "Address", "Email", "Phone", "Department Name")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    students = fetch_students()
    for student in students:
        tree.insert("", tk.END, values=student)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()
   
def display_departments_view():
    def fetch_departments():
        query = "SELECT * FROM Departments"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Departments")

    columns = ("DepartmentID", "DepartmentName")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    departments = fetch_departments()
    for department in departments:
        tree.insert("", tk.END, values=department)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()

def display_courses_view():
    def fetch_courses():
        query = "SELECT * FROM Courses"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Courses")

    columns = ("CourseID", "CourseName", "Credits", "DepartmentName")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    courses = fetch_courses()

    # Iterate through each course to fetch and add the department name
    for course in courses:
        tree.insert("", tk.END, values=course)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()
def display_enrollments_view():
    def fetch_enrollments():
        query = "SELECT * FROM Enrollments"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Enrollments")

    columns = ("EnrollmentID", "StudentID", "CourseID", "EnrollmentDate")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    enrollments = fetch_enrollments()
    for enrollment in enrollments:
        tree.insert("", tk.END, values=enrollment)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()

def display_grades_view():
    def fetch_grades():
        query = "SELECT * FROM Grades"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Grades")

    columns = ("GradeID", "EnrollmentID", "Grade")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    grades = fetch_grades()
    for grade in grades:
        tree.insert("", tk.END, values=grade)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()

def display_faculty_view():
    def fetch_faculty():
        query = "SELECT * FROM Faculty"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Faculty Members")

    columns = ("FacultyID", "Name", "Designation", "Email", "Phone", "DepartmentID")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    faculty_members = fetch_faculty()
    for member in faculty_members:
        tree.insert("", tk.END, values=member)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()

def display_schedules_view():
    def fetch_schedules():
        query = "SELECT * FROM Schedules"
        return execute_query(query)

    display_window = tk.Tk()
    display_window.title("View Schedules")

    columns = ("ScheduleID", "CourseID", "FacultyID", "Day", "Time")
    tree = ttk.Treeview(display_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    schedules = fetch_schedules()
    for schedule in schedules:
        tree.insert("", tk.END, values=schedule)

    tree.pack(expand=True, fill="both")
    display_window.mainloop()
