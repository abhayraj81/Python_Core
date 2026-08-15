# SETS OPERATIONS

# 1. add() - add single element to a set.

fruits = {"apple","banana"}
fruits.add("cherry")
print(fruits)
print(type(fruits))

my_set2 = set([4,5,6])
print(my_set2)

my_set2.add(123)
print(my_set2)
print(type(my_set2))


# 2. remove() 

fruits = {'apple','mango','banana'}
print(fruits)

fruits.remove('mango') #if element not present shows error
print(fruits)

# 3. discard()

fruits.discard("apple") # if element not present doesn't shows error
print(fruits)

