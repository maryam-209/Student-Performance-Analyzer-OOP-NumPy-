import numpy as np
import pandas as pd
# ----------------- Classes -----------------
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = np.array(marks)

class Result:
    def total_marks(self, marks):
        return np.sum(marks)

    def calculate_avg(self, marks):
        return np.average(marks)

    def assign_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
df=pd.DataFrame(columns=["Name","Roll_no","Marks","Average","Grade","Total"])
number_student=int(input("Enter no of students--:- "))
for i in range(number_student):
    print(f"\n students {i+1}") 
    # ----------------- Input -----------------
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = [int(x) for x in input("Enter marks separated by space: ").split()]
    
    # ----------------- Create Objects -----------------
    student1 = Student(name, roll_no, marks)
    result = Result()
    
    # ----------------- Calculations -----------------
    total = result.total_marks(student1.marks)
    average = result.calculate_avg(student1.marks)
    grade = result.assign_grade(average)
    df.loc[len(df)]=(student1.name,student1.roll_no,student1.marks,total,average,grade)
# ----------------- Output -----------------
print("\nStudent:", student1.name)
print("Roll No:", student1.roll_no)
print("Marks:", student1.marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("\n All Students")
print(df)
df.to_csv("Student_data.csv",index=False)
print("Data Saved to Student_data.csv Successfully!")
