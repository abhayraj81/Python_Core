# list methods

my_list = ["apple","banana","cherry"]
print(my_list)

# replace element at index 1

my_list[1] = "blueberry"
print(my_list)

# add element in list 

my_list.append("mango")
print(my_list)
my_list.append(123)
print(my_list)

# remove element from list

my_list.remove("cherry")
print(my_list)


# extend()

fruits = ["peach","grenade"]
dry_fruits = ["cashew","almond"]

fruits.extend(dry_fruits)
print(fruits)

dry_fruits.extend(fruits)
print(dry_fruits)


# insert()

place = ["kanpur","allahbad","delhi"]
place.insert(1,"jammu")
print(place)

# remove()

place.remove("kanpur")
print(place)

# clear()

place.clear()
print(place)

# finding index

names = ["abhay","raj","mehta","aman","amisha","mehta"]
index = names.index("mehta")
print(index)

# finding index with range

index = names.index("mehta",3)
print(index)

# count elements

count = names.count("mehta")
print(count)

# reverse list

names.reverse()
print(names)

# sorting list
numbers = [40,10,30,20]
numbers.sort() 
print(numbers)

# sort in descending order
numbers.sort(reverse=True)
print(numbers)

# sorting with the key
names.sort(key=len)  # sort on the basis of length
print(names)
names.sort(key=len,reverse=True)  # sort on the basis of longest length
print(names)


# pop with default
numbers = [40,10,30,20]
last = numbers.pop()
print(numbers)
print(last)

# pop with index value
numbers = [40,10,30,20]
popped = numbers.pop(2)
print(numbers)
print(popped)

# copy list
fruits = ["apple","banana","cherry"]
copy_fruits = fruits.copy()  # shallow copy
print(copy_fruits)

# modifying copy does not affect original list
copy_fruits.append("mango")
print(copy_fruits)
print(fruits)