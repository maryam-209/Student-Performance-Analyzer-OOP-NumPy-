import numpy as np

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = np.array(marks)

class ResultAnalyzer:
    def average(self, marks):
        return np.mean(marks)

    def highest(self, marks):
        return np.max(marks)

    def lowest(self, marks):
        return np.min(marks)

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.analyzer = ResultAnalyzer()

    def add_student(self):
        name = input("Enter name: ")
        roll = int(input("Enter roll no: "))

        marks = []
        for i in range(3):
            m = int(input(f"Enter marks of subject {i+1}: "))
            marks.append(m)

        student = Student(name, roll, marks)
        self.students.append(student)

        print("Student added successfully!")

    def show_all(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print("Name:", s.name)
            print("Roll:", s.roll_no)
            print("Marks:", s.marks)

            print("Average:", self.analyzer.average(s.marks))
            print("Highest:", self.analyzer.highest(s.marks))
            print("Lowest:", self.analyzer.lowest(s.marks))

            print("----------------------")

    def topper(self):
        top_student = None
        highest_avg = 0

        for s in self.students:
            avg = self.analyzer.average(s.marks)

            if avg > highest_avg:
                highest_avg = avg
                top_student = s

        if top_student:
            print("Topper:", top_student.name)
            print("Average Marks:", highest_avg)

system = SchoolSystem()

while True:
    print("1 Add Student")
    print("2 Show Students")
    print("3 Show Topper")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        system.add_student()

    elif choice == 2:
        system.show_all()

    elif choice == 3:
        system.topper()

    elif choice == 4:
        print("Exited bye!")
        break
    else:
        print("No student found")