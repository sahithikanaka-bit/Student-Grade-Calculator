import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        mark1 = float(subject1_entry.get())
        mark2 = float(subject2_entry.get())
        mark3 = float(subject3_entry.get())

        # Ensure every mark is valid
        if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100):
            messagebox.showerror("Invalid marks", "Enter marks only between 0 and 100.")
            return

        total = mark1 + mark2 + mark3
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        result_label.config(
            text=f"Total Marks: {total}\nAverage: {average:.2f}%\nGrade: {grade}"
        )

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers for all subjects.")


window = tk.Tk()
window.title("Student Marks Calculator")
window.geometry("400x350")

tk.Label(window, text="Student Marks Calculator", font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(window, text="Subject 1 marks (out of 100):").pack()
subject1_entry = tk.Entry(window)
subject1_entry.pack(pady=5)

tk.Label(window, text="Subject 2 marks (out of 100):").pack()
subject2_entry = tk.Entry(window)
subject2_entry.pack(pady=5)

tk.Label(window, text="Subject 3 marks (out of 100):").pack()
subject3_entry = tk.Entry(window)
subject3_entry.pack(pady=5)

tk.Button(window, text="Calculate Result", command=calculate_result).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

window.mainloop()