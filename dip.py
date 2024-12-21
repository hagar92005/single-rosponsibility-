# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:34:23 2024

@author: PCZHRAA
"""

#dip
from abc import ABC, abstractmethod 
class FrontEnd: 
    def __init__(self, data_source): 
        self.data_source = data_source 
        def display_data(self): 
            data = self.data_source.get_data() 
            print("Display data:", data) 
class DataSource(ABC): 
    @abstractmethod 
    def get_data(self): 
        pass 
 
class Database(DataSource): 
    def get_data(self): 
        return "Data from the database" 
 
class API(DataSource): 
    def get_data(self): 
        return "Data from the API"