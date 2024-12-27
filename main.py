from  add import *
from display import *
import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title("University Management System")
    root.geometry("800x600")

    # Navigation buttons
    tk.Button(root, text="Add Student", command=add_student_form).pack(pady=10)
    tk.Button(root, text="View Students", command=display_students_view).pack(pady=10)
    tk.Button(root, text="Add Course", command=add_course_form).pack(pady=10)
    tk.Button(root, text="View Course", command=display_courses_view).pack(pady=10)
    tk.Button(root, text="Add department", command=add_department_form).pack(pady=10)
    tk.Button(root, text="View departments", command=display_departments_view).pack(pady=10)
    tk.Button(root, text="Add Faculty", command=add_faculty_form).pack(pady=10)
    tk.Button(root, text="View Faculties", command=display_faculty_view).pack(pady=10)
    tk.Button(root, text="Add Schedule", command=add_schedule_form).pack(pady=10)
    tk.Button(root, text="View Schedules", command=display_schedules_view).pack(pady=10)

    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    

    root.mainloop()

if __name__ == "__main__":
    main_window()
