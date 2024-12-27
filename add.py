from connection import execute_query
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk

def add_student_form():
    def submit():
        name = name_entry.get()
        dob = dob_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        Department_Name = department_var.get()

        if name and dob and email and phone and Department_Name:
            query = """
                INSERT INTO Students (Name, DOB, Address, Email, Phone, DepartmentName)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            result = execute_query(query, (name, dob, address, email, phone, Department_Name))
            if result is not None:
                messagebox.showinfo("Success", "Student added successfully!")
                add_student_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add student!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    # Form layout
    add_student_window = tk.Tk()
    add_student_window.title("Add Student")

    tk.Label(add_student_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_student_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_student_window, text="DOB (YYYY-MM-DD):").grid(row=1, column=0)
    dob_entry = tk.Entry(add_student_window)
    dob_entry.grid(row=1, column=1)

    tk.Label(add_student_window, text="Address:").grid(row=2, column=0)
    address_entry = tk.Entry(add_student_window)
    address_entry.grid(row=2, column=1)

    tk.Label(add_student_window, text="Email:").grid(row=3, column=0)
    email_entry = tk.Entry(add_student_window)
    email_entry.grid(row=3, column=1)

    tk.Label(add_student_window, text="Phone:").grid(row=4, column=0)
    phone_entry = tk.Entry(add_student_window)
    phone_entry.grid(row=4, column=1)

    tk.Label(add_student_window, text="Department_Name:").grid(row=5, column=0)
    department_var = tk.StringVar(add_student_window)
    department_dropdown = ttk.Combobox(add_student_window, textvariable=department_var)
    query = "SELECT DepartmentName FROM Departments"
    result = execute_query(query)
    department_dropdown['values'] = result
    department_dropdown.grid(row=5, column=1)

    tk.Button(add_student_window, text="Submit", command=submit).grid(row=6, column=0, columnspan=2)
    add_student_window.mainloop()
from tkinter import Tk, Label, Entry, Button, messagebox

def add_department_form():
    # Create the main window
    add_department_window = Tk()
    add_department_window.title("Add Department")

    # Labels and Entries for DepartmentID and DepartmentName
    Label(add_department_window, text="Department ID (Optional):").grid(row=0, column=0)
    department_id_entry = Entry(add_department_window)
    department_id_entry.grid(row=0, column=1)

    Label(add_department_window, text="Department Name:").grid(row=1, column=0)
    department_name_entry = Entry(add_department_window)
    department_name_entry.grid(row=1, column=1)

    def submit():
        # Get the values from the entry fields
        department_id = department_id_entry.get()  # This will be empty if not provided
        department_name = department_name_entry.get()

        # If DepartmentID is provided, try to insert it, otherwise leave it out
        if department_name:
            if department_id:
                query = "INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)"
                result = execute_query(query, (department_id, department_name))
            else:
                # Insert only DepartmentName, leave the auto-increment field to handle DepartmentID
                query = "INSERT INTO Departments (DepartmentName) VALUES (?)"
                result = execute_query(query, (department_name,))
                
            if result is not None:
                messagebox.showinfo("Success", "Department added successfully!")
                add_department_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add department!")
        else:
            messagebox.showerror("Error", "Department Name is required!")

    # Submit button to trigger the submission
    submit_button = Button(add_department_window, text="Add Department", command=submit)
    submit_button.grid(row=2, columnspan=2)

    add_department_window.mainloop()

def add_course_form():
    def submit():
        course_name = course_name_entry.get()
        credits = credits_entry.get()
        Department_Name = department_var.get()

        if course_name and credits and Department_Name:
            query = "INSERT INTO Courses (CourseName, Credits, DepartmentName) VALUES (?, ?, ?)"
            result = execute_query(query, (course_name, credits, Department_Name))
            if result is not None:
                messagebox.showinfo("Success", "Course added successfully!")
                add_course_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add course!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_course_window = tk.Tk()
    add_course_window.title("Add Course")

    tk.Label(add_course_window, text="Course Name:").grid(row=0, column=0)
    course_name_entry = tk.Entry(add_course_window)
    course_name_entry.grid(row=0, column=1)

    tk.Label(add_course_window, text="Credits:").grid(row=1, column=0)
    credits_entry = tk.Entry(add_course_window)
    credits_entry.grid(row=1, column=1)

    tk.Label(add_course_window, text="Department Name:").grid(row=2, column=0)
    department_var = tk.StringVar(add_course_window)
    department_dropdown = ttk.Combobox(add_course_window, textvariable=department_var)
    query = "SELECT DepartmentName FROM Departments"
    result = execute_query(query)
    department_dropdown['values'] = result
    department_dropdown.grid(row=2, column=1)

    tk.Button(add_course_window, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)
    add_course_window.mainloop()

def add_enrollment_form():
    def submit():
        student_id = student_var.get()
        course_id = course_var.get()
        enrollment_date = enrollment_date_entry.get()

        if student_id and course_id and enrollment_date:
            query = "INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate) VALUES (?, ?, ?)"
            result = execute_query(query, (student_id, course_id, enrollment_date))
            if result is not None:
                messagebox.showinfo("Success", "Enrollment added successfully!")
                add_enrollment_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add enrollment!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_enrollment_window = tk.Tk()
    add_enrollment_window.title("Add Enrollment")

    tk.Label(add_enrollment_window, text="Student ID:").grid(row=0, column=0)
    student_var = tk.StringVar(add_enrollment_window)
    student_dropdown = ttk.Combobox(add_enrollment_window, textvariable=student_var)
    student_dropdown['values'] = [1, 2, 3]  # Fetch dynamically
    student_dropdown.grid(row=0, column=1)

    tk.Label(add_enrollment_window, text="Course ID:").grid(row=1, column=0)
    course_var = tk.StringVar(add_enrollment_window)
    course_dropdown = ttk.Combobox(add_enrollment_window, textvariable=course_var)
    course_dropdown['values'] = [1, 2, 3]  # Fetch dynamically
    course_dropdown.grid(row=1, column=1)

    tk.Label(add_enrollment_window, text="Enrollment Date:").grid(row=2, column=0)
    enrollment_date_entry = tk.Entry(add_enrollment_window)
    enrollment_date_entry.grid(row=2, column=1)

    tk.Button(add_enrollment_window, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)
    add_enrollment_window.mainloop()
    
def add_grade_form():
    def submit():
        enrollment_id = enrollment_var.get()
        grade = grade_entry.get()

        if enrollment_id and grade:
            query = "INSERT INTO Grades (EnrollmentID, Grade) VALUES (?, ?)"
            result = execute_query(query, (enrollment_id, grade))
            if result is not None:
                messagebox.showinfo("Success", "Grade added successfully!")
                add_grade_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add grade!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_grade_window = tk.Tk()
    add_grade_window.title("Add Grade")

    tk.Label(add_grade_window, text="Enrollment ID:").grid(row=0, column=0)
    enrollment_var = tk.StringVar(add_grade_window)
    enrollment_dropdown = ttk.Combobox(add_grade_window, textvariable=enrollment_var)
    enrollment_dropdown['values'] = [1, 2, 3]  # Fetch dynamically
    enrollment_dropdown.grid(row=0, column=1)

    tk.Label(add_grade_window, text="Grade:").grid(row=1, column=0)
    grade_entry = tk.Entry(add_grade_window)
    grade_entry.grid(row=1, column=1)

    tk.Button(add_grade_window, text="Submit", command=submit).grid(row=2, column=0, columnspan=2)
    add_grade_window.mainloop()

def add_faculty_form():
    def submit():
        name = name_entry.get()
        designation = designation_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        DepartmentName = department_var.get()

        if name and email and phone and DepartmentName:
            query = """
                INSERT INTO Faculty (Name, Designation, Email, Phone, DepartmentName)
                VALUES (?, ?, ?, ?, ?)
            """
            result = execute_query(query, (name, designation, email, phone, DepartmentName))
            if result is not None:
                messagebox.showinfo("Success", "Faculty member added successfully!")
                add_faculty_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add faculty member!")
        else:
            messagebox.showerror("Error", "All required fields must be filled!")

    add_faculty_window = tk.Tk()
    add_faculty_window.title("Add Faculty Member")

    tk.Label(add_faculty_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_faculty_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_faculty_window, text="Designation:").grid(row=1, column=0)
    designation_entry = tk.Entry(add_faculty_window)
    designation_entry.grid(row=1, column=1)

    tk.Label(add_faculty_window, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(add_faculty_window)
    email_entry.grid(row=2, column=1)

    tk.Label(add_faculty_window, text="Phone:").grid(row=3, column=0)
    phone_entry = tk.Entry(add_faculty_window)
    phone_entry.grid(row=3, column=1)

    tk.Label(add_faculty_window, text="Department ID:").grid(row=4, column=0)
    department_var = tk.StringVar(add_faculty_window)
    department_dropdown = ttk.Combobox(add_faculty_window, textvariable=department_var)
    query = "SELECT DepartmentName FROM Departments"
    result = execute_query(query)
    department_dropdown['values'] = result    
    department_dropdown.grid(row=4, column=1)

    tk.Button(add_faculty_window, text="Submit", command=submit).grid(row=5, column=0, columnspan=2)
    add_faculty_window.mainloop()

def add_schedule_form():
    def submit():
        course_id = course_var.get()
        faculty_id = faculty_var.get()
        day = day_entry.get()
        time = time_entry.get()

        if course_id and faculty_id and day and time:
            query = """
                INSERT INTO Schedules (CourseID, FacultyID, Day, Time)
                VALUES (?, ?, ?, ?)
            """
            result = execute_query(query, (course_id, faculty_id, day, time))
            if result is not None:
                messagebox.showinfo("Success", "Schedule added successfully!")
                add_schedule_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add schedule!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_schedule_window = tk.Tk()
    add_schedule_window.title("Add Schedule")

    tk.Label(add_schedule_window, text="Course ID:").grid(row=0, column=0)
    course_var = tk.StringVar(add_schedule_window)
    course_dropdown = ttk.Combobox(add_schedule_window, textvariable=course_var)
    course_dropdown['values'] = [1, 2, 3]  # Fetch dynamically from Courses table
    course_dropdown.grid(row=0, column=1)

    tk.Label(add_schedule_window, text="Faculty ID:").grid(row=1, column=0)
    faculty_var = tk.StringVar(add_schedule_window)
    faculty_dropdown = ttk.Combobox(add_schedule_window, textvariable=faculty_var)
    faculty_dropdown['values'] = [1, 2, 3]  # Fetch dynamically from Faculty table
    faculty_dropdown.grid(row=1, column=1)

    tk.Label(add_schedule_window, text="Day:").grid(row=2, column=0)
    day_entry = tk.Entry(add_schedule_window)
    day_entry.grid(row=2, column=1)

    tk.Label(add_schedule_window, text="Time (HH:MM:SS):").grid(row=3, column=0)
    time_entry = tk.Entry(add_schedule_window)
    time_entry.grid(row=3, column=1)

    tk.Button(add_schedule_window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)
    add_schedule_window.mainloop()
