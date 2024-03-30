"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import has_word_chain


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


user_input = input("Enter a list of words separated by spaces: ")
words = user_input.split()

word_chain = has_word_chain(words)
print(word_chain)
