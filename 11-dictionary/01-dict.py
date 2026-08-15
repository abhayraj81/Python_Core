#   DICTIONARY

# It is a Data-Structure in python.
# Stores data in key-value pairs known as items.
# dictionaries item are ordered, changeable and do not allow duplicates.
#   Key : must be unique and immutable (string,numbers,tuples)
#   Value: can be any data type and does not need to be unique


#   creating a dictionary

#  syntax : 
#  my_dict = {"key1":"value1","key2":"value2","key3":"value3",......}

# empty dictionary
stu_detail = {}

# 1.dictionary with data
stu_id = {
    "Name":"Abhay Raj",
    "Course":"Python_Core",
    "level":"Beginner"
}
print(stu_id)

# 2. using dict() constructor
person = dict(name="abhay",surname="raj",city="kanpur")
print(person)

# 3. using lists of tulpes
stu = dict([("name","anshika"),("city","goa"),("grade","A+")])
print(stu)
