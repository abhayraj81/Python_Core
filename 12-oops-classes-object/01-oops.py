# OOPs in python

# student details

            # name , grade  
student_1 = ['Madhav', 10] 
student_2 = ['Vishakha', 12]

print(f'{student_1[0]} in class {student_1[1]} ')
print(f'{student_2[0]} in class {student_1[1]} ')


# Oops - creating student records

# class - blueprint or template 
# __init__ method - constructor, value intialize - fix
# self - reference or connection between class and object -fix

class Student:
    def __init__(self, full_name, class_grade, percentage):   # Method-1  
        self.name = full_name           # attribute-1
        self.grade = class_grade        # attribute-2
        self.percentage = percentage    # attribute-3

    def student_details(self):  #Method-2
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")

# object - instance of class

student1 = Student("Abhay Raj",12, 98)
# print(student1.name, student1.grade)

student2 = Student("Raja Sharma",10, 89)
# print(student2.name, student2.grade)

student1.student_details()
student2.student_details()

# print object in form of dictionary
print(student1.__dict__)

# modify object property
student1.percentage = 86
print(student1.percentage)

# delete object property
del student1.percentage
print(student1.__dict__)

# delete object
del student1
print(student1) 