# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:35:22 2024

@author: PCZHRAA
"""

#examples for single rosponsibility 
#example 1
class user:
    def __init__(self , username , email):
        self . username = username
        self . email = email 
        
class UserRepository:
    def save (self , user ):
        print(f"Saving user {user.username} to database.")
        
        
        
class EmailService:
    def sending (self , email , message):
        print(f"sending email {email} : { message}")
        
        
 #example 2
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class OrderProcessor:
    def process_order(self, order):
       
        print(f"Processing order {order.order_id}")

class InvoiceGenerator:
    def generate_invoice(self, order):
        
        print(f"Generating invoice for order {order.order_id}")