#####################
# Day 1
#####################

def day1_p1():
    """
    >>> day1_p1()
    3334297
    """
    ans = 0
    with open("day1input.txt", "r") as file:
        for line in file:
            mass = int(line)
            ans += (mass // 3) - 2
    return ans


def day1_p2():

    def fuel_calculator(mass):
        """Recursively calculates fuel requirement as based on Day 2 puzzle"""
        fuel_needed = (mass // 3) - 2
        if fuel_needed < 0:
            return 0
        else:
            return fuel_needed + fuel_calculator(fuel_needed)

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

from operator import add, mul

def intcode(input_list):
    """Takes in an input list and mutates it accordingly"""

    def intcode_helper(index):
        """Runs one iteration of the intcode program"""
        opcode = input_list[index]
        if opcode == 1:
            operator = add
        elif opcode == 2:
            operator = mul
        elif opcode == 99:
            raise IntcodeException
        else:
            print("you shouldn't see me")

        first_index = input_list[index+1]
        second_index = input_list[index+2]
        output_index = input_list[index+3]

        input_list[output_index] = operator(input_list[first_index], input_list[second_index])

    i = 0
    while i < (len(input_list) - 1):
        try:
            intcode_helper(i)
            i += 4
        except IntcodeException:
            break

def day2_p1():
    with open("day2input.txt", "r") as file:
        contents = file.read()
        input_list_str = contents.split(",")
        input_list = []
        for str in input_list_str:
            input_list.append(int(str))
        # the list is now initialized!
    input_list[1] = 12
    input_list[2] = 2
    intcode(input_list)
    return input_list[0]

class IntcodeException(Exception):
    pass
