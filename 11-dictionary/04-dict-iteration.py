# Dictionaty Iteration

# dict can be iterated using for loop.
# we can loop dictionary by keys, values, or both.

stu = {
    1:"Class-X",
    "name":"Abhay Raj",
    "age":"23",
    "grade":"A",
    "city":"Patna"
}

# 1. loop through keys
for key in stu:
    print(key)

# 2. loop through value
for val in stu:
    print(stu[val]) 

for val in stu.values():
    print(val) 

# 3. loop through key-value pair
for key,value in stu.items():
    print(key,val)