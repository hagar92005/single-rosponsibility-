# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:05:55 2024

@author: PCZHRAA
"""

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.__age = age 

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

Person
person = Person("hagar", 20)
print(person.get_age())  


person.set_age(19)
print(person.get_age())  