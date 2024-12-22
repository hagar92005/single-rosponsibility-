# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:01:19 2024

@author: PCZHRAA
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed
    
    def speak(self):  
        return f"{self.name} barks"


