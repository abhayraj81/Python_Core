# Linking variable with objects

class Student:
    def __init__(self, full_name, class_grade, percentage, team):   # Method-1  
        self.name = full_name           # attribute-1
        self.grade = class_grade        # attribute-2
        self.percentage = percentage    # attribute-3
        self.team = team   # attribute-3

    def student_details(self):  #Method-2
        print(f"{self.name} is in class {self.grade} with {self.percentage}% is in team {self.team}")


team1 = "A"
team2 = "B"

# object - instance of class

student1 = Student("Abhay Raj",12, 98, team1)
# print(student1.name, student1.grade)

student2 = Student("Raja Sharma",10, 89, team2)
# print(student2.name, student2.grade)


student1.student_details()
student2.student_details()