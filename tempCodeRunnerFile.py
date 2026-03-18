
import pandas as pd
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=np.array(marks)
class Result:
    def total_marks(self,marks)