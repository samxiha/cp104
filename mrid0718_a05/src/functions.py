"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-04"
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


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number+1):
        product *= i

    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes.
    Use: calories_burned = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        None
    ------------------------------------------------------
    """
    calories_burned = 0

    for minute in range(5, minutes + 1, 5):
        calories_burned = per_min * minute
        print(f"{minute:2d}   {calories_burned:.1f}")

    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow of # characters pointing up
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the formation 
    Returns:
        None
    -------
    """
    for i in range(rows):
        spaces = " " * (rows - i - 1)
        if i == 0:
            print(spaces + "#")
        else:
            print(spaces + "#" + " " * (2 * i - 1) + "#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(" " * 4, end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:6}", end="")
    print("\n" + " " * 6 + "-" * (6 * (stop_num - start_num + 1)))

    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:6}", end="")
        print()
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, start + count * increment, increment):
        total += i
    return total
