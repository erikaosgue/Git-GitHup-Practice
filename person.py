#!/usr/bin/python3

#THIS should be added in multiple commits
# Exercise to practice git with a simple class

class Person:

    # constructor for Person Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

person1 = Person("Amanda", 22)

#ADD THIS TO 6eabe54 commit
# Print the name and the age of the Person
print(person1.name)
print(person1.age)
person1.myfunc()
