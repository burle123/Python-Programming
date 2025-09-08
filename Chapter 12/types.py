age : int = 25  #variable type hint

def greet(name: str) -> str:   #function type hint
    return f"Hello, {name}! You are {age} years old."

print(greet("Shantanu"))