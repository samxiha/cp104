"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-19"
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


SQUARE_FEET_PER_ACRE = 43560


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = square_feet/SQUARE_FEET_PER_ACRE

    return acres


def lawn_mow_time(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mow_time(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    lawn_area = width * length
    time_minutes = lawn_area / speed

    return time_minutes


def extract_date(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format YYYYMMDD.
    Use: year, month, day = extract_date(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format YYYYMMDD (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number//10000
    month = (date_number//100) % 100
    day = date_number % 100

    return year, month, day


def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = multiply_fractions(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    num = num1 * num2
    den = den1 * den2
    product = num/den

    return num, den, product


def falling_distance(falling_time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        falling_time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    GRAVITY = 9.8
    distance = ((falling_time**2)*GRAVITY)/2

    return distance
