# Furkan Karabulut
# fkarabu
# 04/12/2024
# Lab 11

import tkinter as tk
from tkinter import messagebox

class GradeCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade Calculator")
        
        self.labels = ['Class Activity Average:', 'Lab Average:', 'Project Average:', 'Exam 1 Grade:', 'Exam 2 Grade:', 'Final Exam Grade:']
        self.entries = []
        self.weights = [0.15, 0.15, 0.20, 0.15, 0.15, 0.20]
        
        for i in range(6):
            tk.Label(self, text=self.labels[i]).grid(row=i, column=0)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.entries.append(entry)
            
        self.final_exam_taken = tk.BooleanVar()
        self.final_exam_checkbox = tk.Checkbutton(self, text='Final exam taken',
                                                  variable=self.final_exam_taken)
        self.final_exam_checkbox.grid(row=6, columnspan=2, pady=5)

        # Buttons
        self.compute_button = tk.Button(self, text="Compute Grade", command=self.compute_grade)
        self.compute_button.grid(row=7, column=0, pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=7, column=1, pady=5)

        # Output field
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=8, columnspan=2, pady=5)
        
    def compute_grade(self):
        try:
            grades = [float(entry.get() or 0) for entry in self.entries]
            if not self.final_exam_taken.get():
                grades[-1] = 0  # Set final exam grade to 0 if not taken
                total_weight = sum(self.weights[:-1])
            else:
                total_weight = sum(self.weights)

            final_grade = sum(g * w for g, w in zip(grades, self.weights)) / total_weight
            final_grade = round(final_grade, 2)
            self.result_label.config(text=f"Computed Grade: {final_grade}%")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all grade fields.")

if __name__ == "__main__":
    app = GradeCalculatorGUI()
    app.mainloop()
   

        
    

