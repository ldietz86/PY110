# Practice Problems
# 1 - How would you count the number of occurrences of "banana" in the tuple?
fruits = ("apple", "banana", "cherry", "date", "banana")
print(fruits.count('banana')) # 2

# 2 - What is the set's length? Try to answer without running the code.
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers)) # 5

# 3 - How would you obtain a set that contains all the unique values from both sets?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

merged_set = a.union(b)
merged = a | b
print(merged_set) # {1, 2, 3, 4, 5, 6}
print(merged) # {1, 2, 3, 4, 5, 6}

# 4 - Given the following code, what would the output be? Try to answer without running the code.
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions) 

'''
Output:
{'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty': 3, 'Pebbles': 4, 'Bambam': 5} 
'''

# 5 - Calculate the total age given the following dictionary:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = 0
for value in ages.values():
    total_age += value
    
print(total_age) # 6174

# More concise
total_age = sum(ages.values())
print(total_age) # 6174

# 6 - Determine the minimum age from the above ages dictionary.
min_age = min(ages.values())
print(min_age) # 10

# 7 - What would the following code output?
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words) # ['bear']

# 8 - Given the following string, create a dictionary that represents the frequency with which each letter occurs. 
# The frequency count should be case-sensitive:
statement = "The Flintstones Rock"

letter_frequency = {}

# remove all whitespace characters (" ", \t, \n, \r)
# statement = ''.join(statement.split())

# remove all spaces 
statement = statement.replace(' ', '')
for letter in statement:
    letter_frequency.setdefault(letter, 0)
    letter_frequency[letter] += 1

print(letter_frequency) # {'T': 1, 'h': 1, 'e': 2, 'F': 1, 'l': 1, 'i': 1, 'n': 2, 't': 2, 's': 2, 'o': 2, 'R': 1, 'c': 1, 'k': 1}

# Using the get method
letter_frequency = {}
statement = statement.replace(' ', '')
for letter in statement:
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

print(letter_frequency)

# 9 - What is the return value of the list comprehension below? 
[num for num in [1, 2, 3] if num > 1]
# This will return [2, 3]

# 10 - What does the following code print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem()) # ('b', 'bear)

# 11 - What does the following code return?
lst = [1, 2, 3, 4, 5]
lst[:2]
# This will return [1, 2]

# 12 - What would be the output of the below code? frozen sets are immutable.
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6) # AttributeError: 'frozenset' object has no attribute 'add'
print(frozen)