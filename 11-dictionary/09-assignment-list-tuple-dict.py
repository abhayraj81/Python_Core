# 1. Find the intersection of two lists.
# def intersection_loop(lst1,lst2):
#     common_lst = []
#     for item in lst1:
#         if item in lst2 and item not in common_lst:
#             common_lst.append(item)
#     return common_lst

# list1 = list(map(int, input ("Enter number separated by spaces : ").split()))
# list2 = [int(x) for x in input("Enter number separated by spaces : ").split()]
# print("List 1 : ",list1)
# print("List 2 : ",list2)

# print(intersection_loop(list1,list2))

#                # or

# def intersection(list1,list2):
#     return(item for item in list1 if item in list2)
# print(intersection_loop(list1,list2))

# 2. Find the most frequent element inthe list.
def most_freq(lst):
    max_count = 0
    most_freq = None
    for i in numbers:
        count = lst.count(i)
        if count > max_count:
            max_count = count
            most_freq = i
    return most_freq

numbers = [1,2,2,3,3,3,4,5,6,6,8]
print(most_freq(numbers))

# 3. Find the cummulative Sum of list.
def cummalative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst :
        total += num
        cum_sum.append(total)
    return cum_sum

numbers = [1,2,3,4,5,6,7,9,10]
print(cummalative_sum(numbers))

# 4. Remove Duplicates from a List - 2 methods
def remove_duplicates(lst):
    unique =[]
    seen = set()
    for i in lst :
        if i not in seen:
            unique.append(i)
            seen.add(i)
    return unique

fruits = ["apple","banana","cherry","apple","banana"]
print(remove_duplicates(fruits))

#       or   without seen but not good for large data set
#       using set constructor
print(list(set(fruits)))

# 5. Find the index of the element in a tuple
my_tuple = (1,2,3,4)
def find_index(tup,ele):
    return tup.index(ele) if ele in tup else-1 
print(find_index(my_tuple,3))

# 6. Find the Most frequent value in dictionary
data = {'a':1,'b':2,'c':1,'d':3,'e':1}
def most_freq_ele(dct):
    frequency = {}
    for value in dct.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1
    max_value = max(frequency,key=frequency.get)
    return max_value

print(most_freq_ele(data))

# 7. Merge Dictionaries with summation
def merge_dict(dict1,dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result 

dict1 = {'a':10,'b':20,'c':30}
dict2 = {'b':15,'c':35,'d':25}

print(merge_dict(dict1,dict2))

# 8. Flatten a nested Dictionary
def flatten_dict(data, parent_key='',sep='.'):
    items ={} #initialize empty dict to store flattened items 
    for key, value in data.items():
        # combine current dict with parent key
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            # recursive flatten the nested dict
            items.update(flatten_dict(value, new_key, sep))
        else:
            # adding key - value to flatten dict
            items[new_key] = value
    return items

data = {
    'a':{'b':{'c':42},'d':7},'e':10
    }

print(flatten_dict(data))
print(isinstance(data,dict))

# 9. Sort a dictionary by value
def sorted_by_values(data):
    sorted_items = sorted(data.items(), 
                          key= lambda item:item[1])
    return {key: value for key , value in sorted_items}

data = {'a':5,'b':9,'c':2,'d':7}

print(sorted_by_values(data))

# 10. Access values from a nested dictionary.

data = {
    "level1":{
        "level2":{
            "level3":{
                "value1":10,
                "value2":[1,2,{"deep_key":42}],
                "value3":{"inner_key":"target}"
                },
                "other_key":99
            },
            "list_key":[
                {"inner_key1":88},
                {"inner_key2":{"deep_list_key":77}}
            ]
        }
    }
}

