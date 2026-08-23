# OOPs in python

# student details

            # name , grade  
student_1 = ['Madhav', 10] 
student_2 = ['Vishakha', 12]

print(f' {student_1[0]} in class {student_1[1]} ')
print(f' {student_2[0]} in class {student_1[1]} ')


# Oops - creating student records

# class - blueprint or template 
class Student:
    def __init__(self, full_name, class_grade):        #self : helps to build relation between class and object
        self.name = full_name
        self.grade = class_grade

# object - instance of class
student1 = Student("Abhay Raj",12)
print(student1.name, student1.grade)

