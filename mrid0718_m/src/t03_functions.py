"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants

# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    BASE_COST = 125.00
    COST_PER_SERVICE = 25.00
    VIP_DISCOUNT = 0.9  # 10% off

    num_services = int(input("How many extra services are you purchasing?: "))
    cost = (BASE_COST + (COST_PER_SERVICE * num_services))
    if num_services > 1:
        if_vip = input("Are you a VIP member? (Y/N): ")
        if if_vip == "Y":
            cost *= VIP_DISCOUNT

    return cost
