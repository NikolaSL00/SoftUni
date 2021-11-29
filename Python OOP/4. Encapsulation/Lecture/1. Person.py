# Create a class called Person. Upon initialization, it should receive a name and an age. Name mangle the name and the age attributes (should not be accessed outside the class). Create two instance methods called get_name and get_age to return the values of the private attributes.

# Test Code:
# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())

# Desired Output:
# George
# 32

class Person:

    def __init__(self, name: str, age: int):
        self.__set_name(name)
        self.__set_age(age)

    def __set_name(self, new_name):
        if new_name is None:
            raise "Name can not be None"
        self.__name = new_name

    def __set_age(self, new_age):
        if new_age is None:
            raise "Age can not be None"
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
