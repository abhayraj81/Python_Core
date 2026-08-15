#   SET METHODS

# 1. union() - combines elements from two sets , removing duplicates
set_a = {1,2,3}
set_b = {4,5,6}
union_set = set_a.union(set_b)
print(union_set)


# 2. intersection() - includes elemrnts that are present in both the sets
set_a = {1,2,3}
set_b = {2,3,4}
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# 3. difference() - element present in first set not in second set
set_a = {1,2,3,4}
set_b = {3,4,5}
diff_set = set_a.difference(set_b)
print(diff_set)

# 4. symmetric_difference() - element in either set not in both.
set_a = {1,2,3,4}
set_b = {3,4,5}
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)
sym_diff1 = set_a^set_b
print(sym_diff1)