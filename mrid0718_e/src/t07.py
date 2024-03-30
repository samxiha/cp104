"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from t07_functions import line_lengths
# your imports here

# Your code here
f_in = open("source.txt", "r")
f_short = open("short_lines.txt", "a")
f_long = open("long_lines.txt", "a")

n = int(input("Enter number: "))
short_lines, long_lines = line_lengths(f_in, f_short, f_long, n)

print("Short lines:", short_lines)
print("Long lines:", long_lines)

f_in.close()
f_short.close()
f_long.close()
