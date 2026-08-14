# tuples

# collection of items in ordered
# items in tuple have defined order , that order will not change
# immutable
# allow duplicates
# uses parantheses()

fruits = ("apple","cherry","orange")
print(fruits)
print(type(fruits))

# CREATING A TUPLE

# 1. basic method
my_tuple1 =(1,"Madhav",True,3.14)
print(my_tuple1)
print(type(my_tuple1))

# 2. without parrentheses
my_tuple2 = 1,2,3,4,5
print(my_tuple2)
print(type(my_tuple2))

# 3. tuple constructor method
my_tuple3 = tuple((2,"abhay",2.4))
print(my_tuple3)
print(type(my_tuple3))

list1 = [1,"raj",34.6,'andrew']
my_tuple4 = tuple(list1)
print(my_tuple4)
print(type(my_tuple4))

# 4.  create tuple of single element
my_tuple5 = ("ark",)
print(my_tuple5)
print(type(my_tuple5))

