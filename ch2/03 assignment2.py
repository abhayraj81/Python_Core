# print student name and marks of three subject and percentage
name = input("Enter student name : ")
sub1 = input("Enter marks of English : ")
sub2 = input("Enter marks of Maths : ")
sub3 = input("Enter marks of Science : ")
tmarks = (float(sub1) + float(sub2) + float(sub3))
per = (tmarks/300) * 100
print(f"name\n marks in english : {sub1} \n marks in Maths : {sub2} \n marks in Science {sub3} \n percentage : {int(per)}")

# WAP to collect multiple types of data (eg. name , age , height and student_status) from user and store them in dictionary and print collected data.
s_info = {}
s_info['name'] = input("Enter student name : ")
s_info['age'] = int(input("Enter student age : "))
s_info['height'] = float(input("Enter student's height : "))
s_info['status'] = bool(input("Enter student status(1 for true/ 0 for false) : "))
print(s_info)


