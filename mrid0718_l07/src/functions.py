"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports

# Constants


from random import randint


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


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 1
    guess = int(input("Guess: "))

    while number != guess:
        count += 1

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again")

        guess = int(input("Guess: "))

    print("Congratulations - good guess!")

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1

    while power < target:
        power *= 2

    return power


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    value = float(input("First positive value: "))

    minimum = value
    maximum = value
    total = value
    count = 1

    while value >= 0:
        value = float(input("Next positive value: "))

        if value >= 0:
            count += 1
            total += value
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
    average = total / count

    return minimum, maximum, total, average


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    day = 1
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    another_day = "Y"

    while another_day == "Y":
        print(f'Day {day}\n')
        b_cost = float(input("How much was breakfast? $"))
        l_cost = float(input("How much was lunch? $"))
        s_cost = float(input("How much was supper? $"))

        a_cost = b_cost + l_cost + s_cost
        print(f"Your total for the day was ${a_cost}\n")
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        day += 1

        another_day = input("Were you away another day (Y/N)? ")

    a_total = b_total + l_total + s_total

    return b_total, l_total, s_total, a_total


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    total = 0.0
    employee_count = 0
    TAX_RATE = 3.625/100
    OVERTIME_RATE = 1.5
    OVERTIME = 40

    employee_id = int(input("Employee ID: "))

    while employee_id != 0:
        wage_rate = int(input("Hourly wage rate: "))
        hours = int(input("Hours worked: "))

        if hours > OVERTIME:
            normal_wage = OVERTIME * wage_rate
            overtime_wage = (hours-OVERTIME) * OVERTIME_RATE * wage_rate
            wage = normal_wage + overtime_wage
        else:
            wage = hours * wage_rate

        tax = TAX_RATE * wage
        net_wages = wage - tax
        print(f'Net payment for employee {employee_id}: ${net_wages}\n')
        total += net_wages
        employee_count += 1

        employee_id = int(input("Employee ID: "))
    if employee_count > 0:
        average = total / employee_count
    else:
        average = 0.0

    return total, average
