# Practice Problems: Nested Data Structures

# 1. For each object shown below, demonstrate how you would access the letter g.
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]] 
lst1[2][1][3] # 'g'

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
lst2[1]['third'][0] # 'g'

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
lst3[2]['third'][0][0] # 'g'

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
dict1['b'][1]

dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
list(dict2['3rd'].keys())[0] # 'g'

for key in dict2['3rd'].keys():
    print(key)

# g

# 2. For each of these collection objects, demonstrate how you would change the value 3 to 4.
lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1) # [1, [2, 4], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2) # [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 4]

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1) # {'first': [1, 2, [4]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2) # dict2 = {'a': {'a': ['1', 'two', 4], 'b': 4}, 'b': 5}

# less direct than key access: list(dict2['a'].values())[0][2] = 4

# 3. Given the following code, what will the final values of a and b be?
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a
print(a) # 2
print(b) # [3, 8]

# 4. Given the object shown below, print the name, age, and gender of each family member:
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for member, member_dict in munsters.items():
    print(f"{member} is a {member_dict['age']}-year-old {member_dict['gender']}")
    
'''
Herman is a 32-year-old male
Lily is a 30-year-old female
Grandpa is a 402-year-old male
Eddie is a 10-year-old male
Marilyn is a 23-year-old female
'''