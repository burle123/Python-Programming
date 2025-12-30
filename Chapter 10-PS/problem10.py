#Encapsulation Example in Python

class Dog:
    def __init__(self,name,breed,age):
        self.name=name          # public attribute   
        self._breed=breed       # protected attribute
        self.__age=age          # private attribute

    # Public method to access all info
    def get_info(self):
        return f"Dog Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
 
    # Getter and Setter for private attribute 
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age=age
         
dog=Dog("Buddy","Golden Retriever",3)
print(dog.get_info())         # Accessing public method to get info

print(dog.name)               # Accessing public attribute
print(dog._breed)             # Accessing protected attribute (not recommended)
# print(dog.__age)            # Trying to access private attribute will raise an AttributeError
print(dog.get_age())          # Accessing private attribute via public method
dog.set_age(4)                # Modifying private attribute via public method
print(dog.get_info())         # Verify the age update