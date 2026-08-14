# access range of elemrnts with help of slicing


tuple = (10, 20, 30, 40, 50, 60, 100)
# index   0   1   2   3   4   5   6    
# index  -7  -6  -5  -4  -3  -2  -1

# syntax of slicing : tuple = [start : stop : step]
# start is inclusive (default is index 0)
# stop is exclusive  (default is index -1/lastIndex value)

# first three element of tuple
print(tuple[0:3])

# element from index 1 to 4
print(tuple[1:5])

# last three elements
print(tuple[-3:])

# alternative elements
print(tuple[::2])   # step is 2

# reverse the tuple
print(tuple[::-1])





