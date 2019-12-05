from operator import add, mul, sub

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

def day2_p1():
    """>>> day2_p1()
    7594646
    """
    input_list = original_input()
    input_list[1] = 12
    input_list[2] = 2
    intcode(input_list)
    return input_list[0]

def day2_p2():
    """>>> day2_p2()
    3376
    """
    for noun in range(100):
        for verb in range(100):
            input_list = original_input()
            input_list[1] = noun
            input_list[2] = verb
            intcode(input_list)
            if input_list[0] == 19690720:
                return 100 * noun + verb

def original_input():
    """Returns the input list as provided."""
    with open("day2input.txt", "r") as file:
        contents = file.read()
        input_list_str = contents.split(",")
        input_list = []
        for str in input_list_str:
            input_list.append(int(str))
    return input_list

def intcode(input_list):
    """Takes in an input list and mutates it accordingly"""

    def intcode_helper(index):
        """Runs one iteration of the intcode program"""
        opcode = input_list[index]
        if opcode == 1:
            op = add
        elif opcode == 2:
            op = mul
        elif opcode == 99:
            raise IntcodeException
        else:
            print("you shouldn't see me")

        first_index = input_list[index+1]
        second_index = input_list[index+2]
        output_index = input_list[index+3]

        input_list[output_index] = op(input_list[first_index], input_list[second_index])

    i = 0
    while i < (len(input_list) - 1):
        try:
            intcode_helper(i)
            i += 4
        except IntcodeException:
            break


class IntcodeException(Exception):
    pass

#####################
# Day 3
#####################

def day3_p1():
    distances = list_intersections()
    point = min(distances, key=manhattan)
    return manhattan(point)

def day3_p2():
    distances = list_intersections()
    point = min(distances, key=signal_delay)
    return signal_delay(point)

def manhattan(position, origin=[0, 0]):
    return abs(position[0] - origin[0]) + abs(position[1] - origin[1])

def signal_delay(position):
    all_wires = wire_init()
    step1 = construct_wires(all_wires[0], True, position)
    step2 = construct_wires(all_wires[1], True, position)
    if step1 and step2: #step1 and step2 should never be 0 as intersections don't occur at origin
        return step1 + step2
    else:
        return float('inf')

def list_intersections():
    all_wires = wire_init()
    wire0 = construct_wires(all_wires[0])
    wire1 = construct_wires(all_wires[1])
    distances = []
    for first in wire0:
        for second in wire1:
            i = intersects(first, second)
            if i:
                distances.append(i)
    return distances


def intersects(seg1, seg2):
    """Returns False if no intersection, or an intersection point
    if two line segments intersect.
    """
    def vertical(segment):
        """True if the segment's x coord doesn't change"""
        return segment[0][0] == segment[1][0]

    def horizontal(segment):
        """True if the segment's y coord doesn't change"""
        return segment[0][1] == segment[1][1]

    def point_particle(segment):
        """True if segment is actually a point"""
        return vertical(segment) and horizontal(segment)

    if vertical(seg1) and horizontal(seg2):
        seg1_x = seg1[0][0]
        seg2_x_min = min(seg2[0][0], seg2[1][0])
        seg2_x_max = max(seg2[0][0], seg2[1][0])

        seg2_y = seg2[0][1]
        seg1_y_min = min(seg1[0][1], seg1[1][1])
        seg1_y_max = max(seg1[0][1], seg1[1][1])
    elif vertical(seg2) and horizontal(seg1):
        return intersects(seg2, seg1)
    else:
        return False

    if (
        (point_particle(seg1) and seg2_y == seg1[0][1] and
        seg1_x in range(seg2_x_min, seg2_x_max))
        or
        (point_particle(seg2) and seg1_x == seg2[0][0] and
        seg2_y in range(seg1_y_min, seg1_y_max))
        or
        (
        seg1_x in range(seg2_x_min, seg2_x_max) and
        seg2_y in range(seg1_y_min, seg1_y_max)
        )):
        return [seg1_x, seg2_y]
    else:
        return False


def construct_wires(wire_instructions, intersect_mode=False, point=None):
    """Constructs coordinate objects given a set of instructions as given
    by wire_init().

    An instruction is a string like 'R134', i.e. move right 134 units.

    If in intersect mode, it'll return the number of steps taken to get
    to a given point.
    """
    def wire_helper(dim):
        nonlocal position
        nonlocal distance
        if dim == 'x': # choose which dim to modify
            index = 0
        else:
            index = 1
        first = tuple(position)
        position[index] += distance
        second = tuple(position)
        segment = [first, second]
        if intersect_mode:
            i = intersects(segment, [tuple(point), tuple(point)])
            if i:
                position[index] -= distance
                distance = manhattan(position, i)
                raise WireException('intersection reached')
        wire.append(segment)

    position = [0, 0] # begin at origin
    wire = []
    total_steps = 0
    for instruction in wire_instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == 'R':
            dim = 'x'
        elif direction == 'U':
            dim = 'y'
        elif direction == 'L':
            dim = 'x'
            distance = -distance
        elif direction == 'D':
            dim = 'y'
            distance = -distance
        else:
            print('help')
        try:
            wire_helper(dim)
            total_steps += abs(distance)
        except WireException:
            total_steps += abs(distance)
            return total_steps
    if intersect_mode:
        return 0
    return wire

def wire_init():
    """Returns the instructions to lay down wires as a list of lists"""
    with open("day3input.txt", "r") as file:
        contents = file.read()
        contents_split = contents.splitlines()
        all_wires = []
        for line in contents_split:
            wire = line.split(",")
            all_wires.append(wire)

    return all_wires

class WireException(Exception):
    pass

#####################
# Day 4
#####################

from operator import gt, eq

input_range = range(136760, 595730 + 1)

def day4_p1():
    ans = 0
    for i in input_range:
        if not decreasing(i) and two_adjacent(i):
            ans += 1
    return ans

def day4_p2():
    ans = 0
    for i in input_range:
        if not decreasing(i) and two_adjacent_restrictive(i):
            ans += 1
    return ans


def two_adjacent_restrictive(num):
    """True if an adjacent pair of numbers is eq to each other
    AND has an adjacent sequence 2 numbers long"""

    def largest_block(num, i):
        """Find the greatest number of consecutive instances of i in num.
        If num is 99919919999 and i is 9, the answer should be 4.
        """
        rightmost = num % 10
        ans = 0
        if num == 0:
            return 0
        while num and rightmost != i:
            num //= 10
            rightmost = num % 10
        while num and rightmost == i:
            ans += 1
            num //= 10
            rightmost = num % 10
        return max(ans, largest_block(num, i))

    if two_adjacent(num):
        for i in range(10):
            if largest_block(num, i) == 2:
                return True
    else:
        return False



def two_adjacent(num):
    """True if an adjacent pair of numbers is eq to each other"""
    return compare(num, eq)

def decreasing(num):
    """True if at least one instance of digits decreasing left to right"""
    return compare(num, gt)

def compare(num, op):
    rightmost = num % 10
    second_rightmost = (num // 10) % 10
    if op(second_rightmost, rightmost):
        return True
    elif num > 99:
        return compare(num // 10, op)
    else:
        return False
