#!/usr/bin/python3

# Exercise to practice git with a simple class

class Person:

    # constructor for Person Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)


person1 = Person("Amanda", 22)

# Print the name and the age of the Person
print(person1.name)
print(person1.age)
person1.myfunc()


# Creating a Child class to practice inheritance

class Student(Person):
  pass


student1 = Student("Mike", 21)
student1.myfunc()
