"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """
    DRY = rainfall < 4
    DAMP = 4 <= rainfall <= 8
    WET = rainfall > 8
    dry_days = 0
    damp_days = 0
    wet_days = 0
    days = 0
    rain_amount = 0
    rainfall = int(input("Daily rainfall (mm): "))
    while rainfall != -1:
        rain_amount += rainfall
        days += 1
        rainfall = int(input("Daily rainfall (mm): "))
        if DRY:
            dry_days += 1
        elif DAMP:
            damp_days += 1
        elif WET:
            wet_days += 1

    avg = rain_amount/days
    return dry_days, damp_days, wet_days, avg
