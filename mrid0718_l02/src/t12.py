"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants


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


seconds = int(input("Number of seconds: "))

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600

num_days = seconds // (24 * SECONDS_PER_HOUR)
seconds = seconds % (24 * SECONDS_PER_HOUR)

num_hours = seconds // SECONDS_PER_HOUR
seconds %= SECONDS_PER_HOUR

num_minutes = seconds // SECONDS_PER_MINUTE
seconds %= SECONDS_PER_MINUTE

num_seconds = seconds
print("Days:", num_days, "Hours:", num_hours,
      "Minutes:", num_minutes, "Seconds:", num_seconds)
