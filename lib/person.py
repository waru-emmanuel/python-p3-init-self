#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    

    # Create an instance of the Person class
person = Person("John Doe", 30)

# Print the person object
print(person)

