from typing import List, Dict, Tuple, Union

numbers: List[int] = [1, 2, 3, 4, 5] # List of integers
person: Dict[str, int] = {"Alice": 30, "Bob": 25} # Dictionary with string keys and integer values
coordinates: Tuple[float, float] = (10.0, 20.0) # Tuple of two floats
identifier: Union[int, str] = "ID12345" # Variable that can be either int or str
identifier: Union[int, str] = 12345 # Variable that can be either int or str

print(numbers)
print(person)   
print(coordinates)
print(identifier)

