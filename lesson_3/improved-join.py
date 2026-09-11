'''
Write a function that takes a list as an argument and two optional parameters. The first optional parameter specifies a separator that is used between each
element in the list and the second optional parameter specifies a separator to use between the last two items element in the list.

By default, the separator is a ', ' and the last separator is 'or'

Algo:
If the input list is empty, return an empty string
If the input list has two numbers, separate them with 'or'
If the input list has more than two numbers, use the separator between each number
  - Initialize a variable to hold the last number in the sequence
  - Initialize a variable to hold the result string
  - Loop over the list of numbers up until 1 - length of list
  - Use string interpolation to add a separator after each number and concatenate that string to the result string
  - Insert the last_separator between the last two numbers
    - Use string interpolation to add the last separator before the last number and concatenate that string to the result string
Otherwise, return the number in the list as a string
'''

def join_or(lst, separator=', ', last_separator='or'):
    if not lst:
        return ""
    if len(lst) == 2:
        return f'{lst[0]} {last_separator} {lst[1]}'
    if len(lst) > 2:
        last_num = str(lst[-1])
        result = ""
        for idx in range(len(lst) - 1):
            result += f'{lst[idx]}{separator}'
        result += f'{last_separator} {last_num}'
        return result
    return str(lst[0])

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

# using match/case, join method and slicing notation
def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"

    leading_items = delimiter.join(str(item) for item in sequence[:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'

# using if/else, join and slicing
def join_or(sequence, delimiter=', ', word='or'):
    if len(sequence) == 0:
        return ''

    if len(sequence) == 1:
        return str(sequence[0])

    if len(sequence) == 2:
        return f'{sequence[0]} {word} {sequence[1]}'

    leading_items = delimiter.join(str(item) for item in sequence[:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'