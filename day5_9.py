from operator import add, mul, sub

#####################
# Day 5
#####################

def day5_p1():
    input_list = original_input()
    intcode(input_list, 1)

def intcode(input_list, sys_id, starting_index=0):
    """Takes in an input list and mutates it accordingly.

    sys_id: input for opcode3's program.
    """
    def param_index(param_num, imme_mode):
        """Return the index to search for a parameter"""
        i = index + param_num
        if not imme_mode:
            i = input_list[i]
        return i

    def add_mul(op):
        in1index = param_index(1, p1mode)
        in2index = param_index(2, p2mode)
        out1index = param_index(3, 0) #writing is never in immediate mode
        input_list[out1index] = op(input_list[in1index], input_list[in2index])

    def opcode3(input1):
        out1index = param_index(1, 0)
        input_list[out1index] = input1

    def opcode4():
        out1index = param_index(1, 0)
        print(input_list[out1index])

    running = True
    index = starting_index
    while running and index < (len(input_list) - 1):
        [opcode, p1mode, p2mode, p3mode] = decode_instruction(input_list[index])
        if opcode == 1:
            add_mul(add)
            index += 4
        elif opcode == 2:
            add_mul(mul)
            index += 4
        elif opcode == 3:
            opcode3(sys_id)
            index += 2
        elif opcode == 4:
            opcode4()
            index += 2
        elif opcode == 99:
            running = False
            print('Program halting')
        else:
            raise IntcodeException('Unknown opcode')

def decode_instruction(num):
    opcode = num % 100
    num //= 100
    p1mode = num % 10
    num //= 10
    p2mode = num % 10
    num //= 10
    p3mode = num % 10
    num //= 10
    return [opcode, p1mode, p2mode, p3mode]

def original_input():
    """Returns the input list as provided."""
    with open("day5input.txt", "r") as file:
        contents = file.read()
        input_list_str = contents.split(",")
        input_list = []
        for str in input_list_str:
            input_list.append(int(str))
    return input_list

class IntcodeException(Exception):
    pass
