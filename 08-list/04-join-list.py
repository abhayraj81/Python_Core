# join list

list1 = [1,2]
print(list1)

list2 = ["a","b"]
print(list2)

# using + operator
list3 = list1 + list2
print(list3)

# using append method
for x in list2:
    list1.append(x)     # apending all elemrnt of list2 in list1
print(list1)

# using extend method
list1 = [3,4]
list2 = ["C","D"]
list1.extend(list2)
print(list1)

