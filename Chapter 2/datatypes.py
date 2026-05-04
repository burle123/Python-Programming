a = 1 # a is an integer

b = 5.22 # b is a floating point number

c = "Harry" # c is a string

d = False # d is a boolean variable

e = None # e is a none type variable

#Integers

# a = 12
# print(f"The id of a is {id(a)} and the value of a is {a}") # The id of a changes because integers are immutable


# spice_mix = set()
# print(f"Initial spice mix id: {id(spice_mix)}")

# spice_mix.add("cumin")
# spice_mix.add("coriander")

# print(f"Spice mix id after adding cumin and coriander: {id(spice_mix)}")  # id remains the same because sets are mutable
 
#Boolean

is_boiling = True
stri_count = 10
total_actions = is_boiling + stri_count
print(f"Total actions: {total_actions}")  # op - 11. The boolean value `True` is treated as `1` in arithmetic operations, so `is_boiling + stri_count` results in `1 + 10`, which equals `11`.


# import sys

# ideal_temp = 95.3
# # current_temp = 95.299999   # op - 9.999999974752427e-07
# current_temp = 95.2
# temp_diff = ideal_temp - current_temp
# print(f"Temperature difference: {temp_diff}")  # op - 0.09999999999999432
# print(f"Information about float: {sys.float_info}")   # sys.float_info - This will print detailed information about the float data type, including its precision, maximum and minimum values, and other characteristics.

#String

# greeting = "Hello, World!"
# print(greeting)  # Output: Hello, World!
# print(greeting[0]) 
# print(greeting[0:12])   
# print(greeting[-1])

# print(greeting[::-1])  # Output: !dlroW ,olleH (reverses the string)

#Encodding and Decoding

# original_string = "Hello, World!"
# encoded_string = original_string.encode('utf-8')
# print(encoded_string)  # Output: b'Hello, World!'
# decoded_string = encoded_string.decode('utf-8')
# print(decoded_string)  # Output: Hello, World!

# Tuples

#swapping values using tuples

tup = (1, 2, 3)
print(f"Original tuple: {tup}")  # Output: Original tuple: (1, 2, 3)

(a, b, c) = tup
print(f"Values unpacked from tuple: a={a}, b={b}, c={c}")  # Output: Values unpacked from tuple: a=1, b=2, c=3

#Lists

#methods of list

# my_list = [1, 2, 3]
# print(f"Original list: {my_list}") 
# my_list.append(4)
# print(f"List after appending 4: {my_list}")  # Output: List after appending 4: [1, 2, 3, 4]
# my_list.remove(2)
# print(f"List after removing 2: {my_list}")  # Output: List after removing 2: [1, 3, 4]
# my_list.insert(1, 5)
# print(f"List after inserting 5 at index 1: {my_list}")  # Output: List after inserting 5 at index 1: [1, 5, 3, 4]
# my_list.pop()
# print(f"List after popping the last element: {my_list}")  # Output: List after popping the last element: [1, 5, 3]
# my_list.sort()
# print(f"List after sorting: {my_list}")  # Output: List after sorting: [1, 3, 5]
# my_list.reverse()
# print(f"List after reversing: {my_list}")  # Output: List after reversing: [5, 3, 1]
# my_list.extend([6, 7])
# print(f"List after extending with [6, 7]: {my_list}")  # Output: List after extending with [6, 7]: [5, 3, 1, 6, 7]

# print(f"Maximum value in the list: {max(my_list)}")  # Output: Maximum value in the list: 7
# print(f"Minimum value in the list: {min(my_list)}")  # Output: Minimum value in the list: 1



# bytearray

# ba = bytearray(4)
# print(ba) # Output: bytearray(b'\x00\x00\x00\x00')
# # Modify the first byte
# ba[0] = 65 # ASCII value for 'A'
# print(ba) # Output: bytearray(b'A\x00\x00\x00')


#Sets

# essential_spices = {"cumin", "coriander", "turmeric"}
# optional_spices = {"cumin", "coriander", "turmeric", "paprika", "garam masala"}
# print(f"Essential spices: {essential_spices}")  
# print(f"Optional spices: {optional_spices}")  


# all_spices = essential_spices.union(optional_spices)
# print(f"All spices: {all_spices}")  # Output: All spices: {'cumin', 'coriander', 'turmeric', 'paprika', 'garam masala'}

# common_spices = essential_spices.intersection(optional_spices)
# print(f"Common spices: {common_spices}")  # Output: Common spices: {'cumin', 'coriander', 'turmeric'}

# only_essential = essential_spices.difference(optional_spices)
# print(f"Spices only in essential: {only_essential}")  # Output: Spices only in essential: set()
# only_optional = optional_spices.difference(essential_spices)
# print(f"Spices only in optional: {only_optional}")  # Output: Spices only in optional: {'paprika', 'garam masala'}


#Dictionaries

chai_recipe = {
    "tea_leaves": "2 tsp",
    "water": "1 cup",
    "milk": "1/2 cup",
    "sugar": "1 tsp",
    "spices": ["cardamom", "cinnamon", "ginger"]
}

print(f"Chai recipe: {chai_recipe}") 

spices = chai_recipe["spices"]
print(f"Spices in the chai recipe: {spices}")  
chai_recipe["sugar"] = "2 tsp"
print(f"Updated chai recipe: {chai_recipe}")



