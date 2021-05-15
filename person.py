#!/usr/bin/python3

# Exercise to practice git with a simple class

class Person:

    # constructor for Person Class
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Amanda", 22)

# Print the name and the age of the Person
print(person1.name)
print(person1.age)
