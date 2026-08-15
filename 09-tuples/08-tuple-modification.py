# TUPLE MODIFICATION

# Typecast tuple in list first
# then do modification
# then again typecast to tuple

tuple_A = (1, 'raj', 122.4, "AG")
print(tuple_A)

list_A = list(tuple_A)
print(list_A)

list_A[1] = 100
print(list_A)

tuple_A = tuple(list_A)
print(tuple_A)