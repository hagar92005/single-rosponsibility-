# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:48:26 2024

@author: PCZHRAA
"""
#Overloading
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c
calc = Calculator()
print(calc.add(2, 3))  
print(calc.add(2, 3, 4))



#Overriding
class Animal:
    def speak(self):
        return "Some generic animal sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
animal = Animal()
dog = Dog()
print(animal.speak()  
print(dog.speak())