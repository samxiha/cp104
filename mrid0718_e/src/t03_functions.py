"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        altered - the resulting string (str)
    -------------------------------------------------------
    """
    VOWELS = 'aeiou'
    altered = ''
    for char in string:
        if char.isalpha():
            if char.lower() in VOWELS:
                altered += char.upper()
            else:
                altered += char.lower()
        else:
            altered += char
    return altered
