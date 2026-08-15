# SETS

# - Collection of uniue items.
# - Do not allow duplicate.
# - Do not maintain particular order so can't be indexed .


#               Characteristics Of SETS
#   - unordered
#   - unique element
#   - mutable : add or remove element after creation
#   - immutable element : individual element inside set can't be modified/replaced


vowels = {'a','e','i','o','u'}


# CREATING SETS

# 1. Using Curly Braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Using Set Constructor
my_set = set([1,2,3,4,5])
print(my_set)


# NOTE : Empty set can't be created using {} as it creates empty dictionary use set() instead .

empty_set = set()
print(empty_set)

