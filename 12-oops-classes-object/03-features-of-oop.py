# 4 feature in oop

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

print("\n : Abstraction : \n")

# 1.Abstraction : Hiding unnecessary details from user through class, method.

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

################################################################################

print("\n : Encapsulation : \n")

# 2.Encapsulation : Restrict the access to certain attribute or methods to protect data and enforce controlled access

class Student:
    def __init__(self, full_name, class_grade, percentage):   # Method-1  
        self.name = full_name               # attribute-1
        self.grade = class_grade            # attribute-2
        self.__percentage = percentage      # attribute-3
        # double underscore limits the access

    def get_percentage(self):               # Best practice to call Encapsulated object by method name initiated by Get. 
        return self.__percentage

    def student_details(self):              #Method-2
        print(f"{self.name} is in class {self.grade} with {self.get_percentage()}%")
                                                        # accessed by get_percentage()
                                                   
student1 = Student("Abhay Raj",12, 98)
student2 = Student("Raja Sharma",10, 89)

# print(student1.__percentage)  Error
# print(student1.__percentage)  Error

student1.student_details()
student2.student_details()

################################################################################

print("\n : Inheritance : \n")

# 3.Inheritance : Allows one class (child) to reuse the prop and methods of another class (parent).

# parent class -
class Student:
    def __init__(self, full_name, class_grade, percentage):   # Method-1  
        self.name = full_name           # attribute-1
        self.grade = class_grade        # attribute-2
        self.percentage = percentage    # attribute-3

    def student_details(self):  #Method-2
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")
                                                  
student1 = Student("Abhay Raj",12, 98)
student2 = Student("Raja Sharma",10, 89)

# child class
class GraduateStudent(Student):                           # child class Graduate student inherit prop. from student parent class.
    def __init__(self, name, grade, percentage, stream):  # parameter from parent class and new parameter in child class
        super().__init__(name, grade, percentage)         # call parent class init
        self.stream = stream                              # new attribute in child class

    def student_details(self):
        super().student_details()                         # method inherit
        print(f'Stream is {self.stream}')

# Object
Grad_Student1 =  GraduateStudent("Anshika", 12, 92, 'PCM')
Grad_Student2 =  GraduateStudent("Ishika", 11, 86, 'PCB')

Grad_Student1.student_details()
Grad_Student2.student_details()

################################################################################

print("\n : Ploymorphism : \n")

# 4.Polymorphism : 
