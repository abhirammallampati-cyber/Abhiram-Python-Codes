import math
import random

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return True
        else:
            return False


def check_student(student):
    try:
        if student.result():
            print(student.name, "has passed!")
        elif student.marks == 0:
            print(student.name, "has no marks.")
        else:
            print(student.name, "has failed.")

    except Exception as error:
        print("Error:", error)
students = [
    Student("Rahul", 85),
    Student("Priya", 35),
    Student("Aman", 0)
]

for student in students:
    check_student(student)

    if student.marks > 80:
        print("Excellent!")
    elif student.marks >= 40:
        print("Good job!")
    else:
        print("Try again!")

count = 0


while count < 3:
    print("Random number:", random.randint(1,10))
    count +=1

numbers = [1,2,3,4,5]

squares = [x**2 for x in numbers if x > 2]
print("Squares:", squares)

with open("students.txt", "w") as file:
    file.write("Student results completed.")
print("Math value:", math.sqrt(25))