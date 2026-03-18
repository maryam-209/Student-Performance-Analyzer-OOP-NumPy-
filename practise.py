import numpy as np
import pandas as pd
class Student:
    def __init__(self,name,roll_no,marks):
        self.name  =name
        self.roll_no  =roll_no
        self. marks =np.array(marks)
class Result:
    def total_avg(self,marks):
        return np.sum(marks)
    def calculate_avg(self,marks):
        return np.average(marks)
    def Assign_grade(self,average):
        if average>=90:
            return 'A'
        elif average>=80:
            return 'B'
        elif average>=70:
            return 'C'
        elif average>=60:
            return 'D'
        else:
            return 'F'
df = pd.DataFrame(columns=["Name", "Roll No", "Marks", "Total", "Average", "Grade"])
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print(f"\nStudent {i+1}:")
    name=input("enter tour name--:- ")
    roll_no=input("Enter your roll no--:- ")
    marks=[int(x) for x in input("enter yor marks with space--:- "). split()] 
    student1=Student(name,roll_no,marks)
    result=Result()
    Total=result.total_avg(student1.marks)
    average=result.calculate_avg(student1.marks)
    grade=result.Assign_grade(average)
    df.loc[len(df)] = [student1.name, student1.roll_no, student1.marks,     Total, average, grade]
print("\n Name: ",student1.name)
print("Roll no: ",student1.roll_no)
print("Marks: ",student1.marks)
print("Total: ",Total)
print("Average of your Marks: ",average)
print("Grade: ",grade)        
print("\n All studentData!")
print(df)       
df.to_csv("Maryam.csv",index=False)
print("Data saved in Maryam.csv successfully!")