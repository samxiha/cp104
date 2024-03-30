"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import student_stats


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


file_handle = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file_handle)
print(f'{l_id}, {h_id}, {avg}')
