import numpy as np
import pandas as pd
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=np.array(marks)
class Result:
    def total_marks(self,marks):
        return np.sum(marks)
    def calculate_avg(self,marks):
        return np.average(marks)
    def Assign_grades(self,average):
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
df=pd.DataFrame(columns=["NAME","ROLL_NO","MARKS","AVERAGE","TOTAL","GRADE"])
count_name=int(input("Enter the number of students you want to add here---: "))
for i in range(count_name):
    print(f"Students: {i+1}")
    name=input(f"Enter name of student {i+1}--:- ") 
    roll_no=int(input("Enter roll no of student "))
    marks=[int(x) for x in input("Enter name of subjects by spacing---: ").split()]
    studen1=Student(name,roll_no,marks)
    result=Result()
    total=result.total_marks(studen1.marks)
    average=result.calculate_avg(studen1.marks)
    grade=result.Assign_grades(average)
    df.loc[len(df)]=(studen1.name,studen1.roll_no,studen1.marks,average,total,grade)
print("\n NAme ",studen1.name)           
print("Roll No ",studen1.roll_no)     
print("Marks ",studen1.marks)  
print("Average: ",average)
print("Total: ",total) 
print("Grage: ",grade)
print("\n All Students")
print(df)
df.to_csv("Maryam.csv",index=False)
print("Data Saved in Maryam.csv Successfuly!")
                
