#####################
# Day 1
#####################

def day1_part1():
    """
    >>> day1_part1()
    3334297
    """
    ans = 0
    with open("day1input.txt", "r") as file:
        for line in file:
            mass = int(line)
            ans += (mass // 3) - 2
    return ans

def fuel_calculator(mass):
    """Recursively calculates fuel requirement as based on Day 2 puzzle"""
    fuel_needed = (mass // 3) - 2
    if fuel_needed < 0:
        return 0
    else:
        return fuel_needed + fuel_calculator(fuel_needed)

def day1_part2():
    ans = 0
    with open("day1input.txt", "r") as file:
        for line in file:
            module_mass = int(line)
            module_fuel = fuel_calculator(module_mass)
            ans += module_fuel
    return ans

#####################
# Day 2
#####################

def day2_part1():
    with open("day2input.txt", "r") as file:
