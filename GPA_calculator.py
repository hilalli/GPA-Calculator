import tkinter as tk
from tkinter import messagebox


def calculate_gpa():
    try:
        total_credits = 0
        total_points = 0
        result_text = ""
        for course in courses:
            ects = float(course['ects'].get())
            if ects < 1 or ects > 8:
                messagebox.showerror("Error", f"ECTS value must be between 1 and 8 for course {course['name'].get()}.")
                return
            grade = course['letter_grade'].get()
            if grade not in grade_points:
                messagebox.showerror("Error", f"Grade value must be a valid letter grade '{grade}' for course {course['name'].get()}.")
                return
            points = grade_points[grade]
            total_credits += ects
            total_points += points * ects
            result_text += f"{course['name'].get()}: {grade} ({points} points)\n"

        if total_credits == 0:
            messagebox.showerror("Error", "Total credits cannot be zero.")
            return

        gpa = total_points / total_credits
        gpa = round(gpa, 2)
        result_var.set(f"GPA: {gpa}\n\nDetails:\n{result_text}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for ECTS.")


def show_grade_meanings():
    meanings = "\n".join([f"{grade}: {meaning}" for grade, meaning in grade_meanings.items()])
    messagebox.showinfo("Grade Meanings", meanings)


# Creating main window
root = tk.Tk()
root.title("ECTS and GPA Calculator")

# Grade points dictionary
grade_points = {
    'AA': 4.0,
    'BA': 3.5,
    'BB': 3.0,
    'CB': 2.5,
    'CC': 2.0,
    'DC': 1.5,
    'DD': 1.0,
    'FF': 0.0
}

# Grade meanings dictionary
grade_meanings = {
    'AA': 'Excellent',
    'BA': 'Very Good',
    'BB': 'Good',
    'CB': 'Satisfactory',
    'CC': 'Pass',
    'DC': 'Conditional Pass',
    'DD': 'Poor',
    'FF': 'Fail'
}

# List to store course details
courses = []

# Adding input fields for courses
frame_courses = tk.Frame(root)
frame_courses.pack(padx=10, pady=10)


def add_course():
    course_frame = tk.Frame(frame_courses)
    course_frame.pack(pady=5)

    tk.Label(course_frame, text="Course Name:").pack(side=tk.LEFT)
    course_name = tk.Entry(course_frame)
    course_name.pack(side=tk.LEFT, padx=5)

    tk.Label(course_frame, text="ECTS:").pack(side=tk.LEFT)
    course_ects = tk.Entry(course_frame)
    course_ects.pack(side=tk.LEFT, padx=5)

    tk.Label(course_frame, text="Letter Grade:").pack(side=tk.LEFT)
    course_grade = tk.Entry(course_frame)
    course_grade.pack(side=tk.LEFT, padx=5)

    courses.append({
        'name': course_name,
        'ects': course_ects,
        'letter_grade': course_grade
    })


# Button to add a new course
button_add_course = tk.Button(root, text="Add Course", command=add_course)
button_add_course.pack(pady=5)

# Adding Calculate button
button_calculate = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
button_calculate.pack(pady=10)

# Adding Show Grade Meanings button
button_meanings = tk.Button(root, text="Show Grade Meanings", command=show_grade_meanings)
button_meanings.pack(pady=5)

# Adding result display
result_var = tk.StringVar()
label_result = tk.Label(root, textvariable=result_var, font="lucida 12 bold")
label_result.pack(pady=10)

# Running the main loop
root.mainloop()
