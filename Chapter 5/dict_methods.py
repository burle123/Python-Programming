marks={
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
print(marks)
#Methods
print(marks.keys())  # Get all keys
print(marks.values())  # Get all values
print(marks.items())  # Get all key-value pairs
print(marks.get("Bob"))  # Accessing value by key using get()
marks.update({"Eve": 88})  # Adding a new key-value pair using update
print(marks)
print(marks.pop("Charlie"))  # Removing a key-value pair using pop
print(marks)
print(marks.clear())  # Clearing the dictionary
print(marks)