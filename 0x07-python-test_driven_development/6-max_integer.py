#!/usr/bin/python3
"""
Module: find_max_integer
Description: Finds the max integer in a list.
"""

def max_integer(lst=[]):
    """
    Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.
    """
    # Check if the list is empty, return None if true
    if len(lst) == 0:
        return None
    
    # Initialize the result with the first element of the list
    result = lst[0]
    
    # Iterate through the list to find the max integer
    m = 1
    while m < len(lst):
        if lst[m] > result:
            result = lst[m]
        m += 1
    
    return result
