# 4 feature in oop

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction : Hiding unnecessary details from user through class, method

class Student:
    def __init__(self, full_name, class_grade, percentage):   # Method-1  
        self.name = full_name           # attribute-1
        self.grade = class_grade        # attribute-2
        self.percentage = percentage    # attribute-3

    def student_details(self):  #Method-2
        print(f"{self.name} is in class {self.grade} with {self.percentage+2}%")
                                                    # hidden from user 
                                                    # given grace +2 percentage to students

student1 = Student("Abhay Raj",12, 98)
student2 = Student("Raja Sharma",10, 89)

student1.student_details()
student2.student_details()