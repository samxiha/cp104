"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-06"
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


length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_cost = float(input("Cost of concrete ($/m^3): "))
brick_cost = float(input("Cost of bricks ($/m^2): "))

foundation_volume = length * width * height
foundation_concrete_cost = foundation_volume * concrete_cost

wall_area = 2*(length * wall_height + width * wall_height)
brick_wall_cost = wall_area * brick_cost

total_cost = foundation_concrete_cost + brick_wall_cost

print(f'\nConcrete needed for foundation (m^3): {foundation_volume:,.2f}')
print(f'Cost of concrete: {foundation_concrete_cost:,.2f}')
print(f'Bricks needed for walls (m^2): {wall_area:,.2f}')
print(f'Cost of bricks: {brick_wall_cost:,.2f}')
print(f'Total cost: {total_cost:,.2f}')
