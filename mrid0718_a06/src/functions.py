"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-11"
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


def total_wins():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings that represent the 
    output of a game with a loop. The user should enter an empty string
    to signal the end of the series. The function returns two numbers 
    representing how many times the string "purple" and how many times 
    the string "gold" appeared in the input.
    Use: purple, gold = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purple - number of times "purple" appeared (str)
        gold - number of times "gold" appeared (str)
    -------------------------------------------------------
    """
    purple = 0
    gold = 0
    team = input("Enter the winning team: ")
    while team != '':
        if team == "purple":
            purple += 1
        elif team == "gold":
            gold += 1

        team = input("Enter the winning team: ")
    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    divisor = 2
    prime = True
    while divisor * divisor <= number:
        if number % divisor == 0:
            prime = False
        divisor += 1

    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_interest_rate = (interest_rate / 100) / 12

    month = 1
    balance = principal_amount

    # Print header
    print(f"Principal:  ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print(f"{'Month':<5}{'Interest':>10}{'Payment':>10}{'Balance':>9}")
    print("----------------------------------")

    while balance > 0:
        interest = balance * monthly_interest_rate

        if payment >= balance + interest:
            payment = balance + interest
        balance = max(balance + interest - payment, 0)
        print(f"{month:>5}{interest:>8.2f}{payment:>12.2f}{balance:>9.2f}")
        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if number < 0:
        number = -number
    while number != 0:
        number //= 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor

        divisor += 1

    return total
