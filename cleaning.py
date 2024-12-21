# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:39:54 2024

@author: PCZHRAA
"""

def calculate_factorial(number: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        number (int): A non-negative integer.
        
    Returns:
        int: The factorial of the given number.
    
    Raises:
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    
    return factorial