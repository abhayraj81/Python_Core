#   SET common uses

#   1. removing duplicates
#   2. membership testing
#   3. set operations : union, intersection and difference
#   4. data analysis : useful in scenarios requiring unique items, such as tags, categories, or unique identifiers.


# removing duplicates examples

numbers = [1,2,3,4,5,6,6,7,2,5,7,9,6,2,10,23,23,10]
unique_numbers = set(numbers)
print(unique_numbers)
