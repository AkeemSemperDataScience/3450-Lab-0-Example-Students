import pandas as pd
import numpy as np

def numberAdder(num_1, num_2):
    """
    Adds two numbers together.
    """
    return num_1 + num_2

def vowelsInString(string):
    """
    Counts the number of vowels in a given string.
    """
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in string if char in vowels)
    return count