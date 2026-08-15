# Dictionary Methods

stu = {
    1:"Class-X",
    "name":"Abhay Raj",
    "age":"23",
    "grade":"A",
    "city":"Patna"
}
print(stu)


# 1.keys() - return all the keys 
print(stu.keys())


# 2.values() - return all the values
print(stu.values()) 


# 3.items - return in form of list of tuples
print(stu.items())


# 4.get() - return value by entering the key
print(stu.get("name"))
# print(stu['email']) -return error as value is not present
print(stu.get('email')) # return None
print(stu.get('email','nahi hai email')) # return given default value if item not available


# 5.Add/Modify items in dictionary

# add item - assign operator
stu['E-mail'] = 'abhay@example.com'
print(stu)

# modify/replace item - assign operator
stu['grade'] = 'A+'
print(stu)

# remove items 
# del to remove items
del stu['grade']
print(stu)
# pop method
del_item = stu.pop('E-mail')
print(stu)
print(del_item)