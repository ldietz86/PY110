# Practice Problems: Comprehensions

# 1. Compute and display the total age of the family's male members. Try working
# out the answer two ways: first with an ordinary loop, then with a comprehension.
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# for loop
total_age = 0

for member_dict in munsters.values():
    if member_dict['gender'] == 'male':
        total_age += member_dict['age']
 
print(total_age) # 444

# list comprehension
print(sum([member_dict['age'] for member_dict in munsters.values()
           if member_dict['gender'] == 'male'])) # 444

# 2. Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order.
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result
[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# The string values should be sorted as strings, while the numeric values should be sorted as numbers.

# for loop
sorted_list = []

for sub_list in lst:
    sorted_list.append(sorted(sub_list))

print(sorted_list) # [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# list comprehension
sorted_list = [sorted(sub_list) for sub_list in lst]
print(sorted_list) # [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# 3. Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order as strings.
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]


# for loop 
sorted_list = []

for sub_list in lst:
    sorted_list.append(sorted(sub_list, key=str))

print(sorted_list) 

# list comprehension
sorted_list = [sorted(sub_list, key=str) for sub_list in lst]
print(sorted_list)

# 4. Write some code that uses comprehensions to define a dictionary where the key 
# is the first item in each sublist, and the value is the second.
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Expected result
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}

new_dict = {sub_list[0]: sub_list[1] for sub_list in lst}
print(new_dict)
'''
Output:
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}
'''

# using the dict constructor
dict(lst)

# 5. Sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain.
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# Expected result
[[1, 8, 3], [1, 6, 7], [1, 5, 3]] 

# for loop 
def sum_odd(nums_lst):
    odd_sum = 0
    for num in nums_lst:
        if num % 2 == 1:
            odd_sum += num
    return odd_sum

sorted_list = sorted(lst, key=sum_odd)
print(sorted_list) # [[1, 8, 3], [1, 6, 7], [1, 5, 3]] 
   
# list comprehension ✧ re-factor sum_odd function
def sum_odd(nums_lst):
    return sum([num for num in nums_lst if num % 2 != 0])

# 6. Given the following data structure, return a new list identical in structure to the original, but 
# with each number incremented by 1. Do not modify the original data structure. Use a comprehension.
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# Expected result
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# for loop 
result = []

for sub_dict in lst:
    incremented_dict = {}
    for key, value in sub_dict.items():
        incremented_dict.update({key: value + 1})
    result.append(incremented_dict)

print(result) # [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# list comprehension ✧         
result = [{key: value + 1 for key, value in sub_dict.items()} for sub_dict in lst]
print(result) # [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# 7. Given the following data structure return a new list identical in structure to the original, but 
# containing only the numbers that are multiples of 3
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# Expected result
[[], [3, 12], [9], [15, 18]]

# for loop
multiples_of_3 = []

for sublist in lst:
    multiples = []
    for item in sublist:
        if item % 3 == 0:
            multiples.append(item)
    multiples_of_3.append(multiples)
    
print(multiples_of_3) # [[], [3, 12], [9], [15, 18]]

# list comprehension ★ 
[[num for num in sublist if num % 3 == 0] for sublist in lst] # [[], [3, 12], [9], [15, 18]]

# 8. Given the following data structure, write some code to return a list that contains the colors of the 
# fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# for loop 
result = []

for name, info_dict in dict1.items():
    if info_dict['type'] == 'fruit':
        capitalized = []
        for color in info_dict['colors']:
            capitalized.append(color.capitalize())
        result.append(capitalized)
    else:
        result.append(info_dict['size'].upper())  

print(result) # [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']          
                   
# list comprehension ✧
result = [
    [color.capitalize() for color in info_dict['colors']]
    if info_dict['type'] == 'fruit'
    else info_dict['size'].upper()
    for name, info_dict in dict1.items()
]

# using a helper function
def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result) # [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']


# 9. Write some code to return a list that contains only the dictionaries where all the numbers are even.
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Expected output
[{'e': [8], 'f': [6, 10]}]

# for loop
even_dicts = []

for dictionary in lst:
    if all(all(n % 2 == 0 for n in values) for values in dictionary.values()):
        even_dicts.append(dictionary) 
        
print(even_dicts) # [{'e': [8], 'f': [6, 10]}]       

# list comprehension ✧ readable
def list_is_even(lst):
    return all([num % 2 == 0 for num in lst])

def all_even(dictionary):
    lists_are_even = [list_is_even(list_value)
                      for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst
                     if all_even(dictionary)]
print(result)

# list comprehension ✧ concise
def all_even(dictionary):
    for values in dictionary.values():
        if not all([num % 2 == 0 for num in values]):
            return False

    return True

result = [val for val in lst if all_even(val)]
print(result)

# 10. Write a function that takes no arguments and returns a string that contains a UUID.
import random

def generate_uuid():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    result = ''
    for _ in range(32):
        random_char = random.choice(characters)
        result += random_char
    
    # manual slicing
    return f'{result[0:8]}-{result[8:12]}-{result[12:16]}-{result[16:20]}-{result[20:]}'

print(generate_uuid())

# pythonic
import random

def generate_uuid():
    characters = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]

    return '-'.join(
        ''.join(random.choice(characters) for _ in range(section))
        for section in sections
    )

print(generate_uuid())

# 11. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Start by trying to write this using nested loops.
list_of_vowels = []

for word_list in dict1.values():
    for word in word_list:
        for char in word:
            if char in 'aeiou':
                list_of_vowels.append(char)
   
print(list_of_vowels) # ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Extra Challenge: Once your nested loop code works, try to refactor the code so it uses a single list comprehension. (You can print the resulting list outside of the comprehension.)
list_of_vowels = [
    char
    for word_list in dict1.values()
    for word in word_list
    for char in word
    if char in 'aeiou'
]

print(list_of_vowels)
