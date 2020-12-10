from operator import add, mul, sub, lt, eq

#####################
# Day 5
#####################

def day5_p1():
    input_list = original_input()
    intcode(input_list, 1)

def day5_p2():
    input_list = original_input()
    intcode(input_list, 5)

def test():
    input_list = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
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

    def index_increment(num):
        """Moves index pointer forward"""
        nonlocal index
        index += num

    def add_mul(op):
        in1index = param_index(1, p1mode)
        in2index = param_index(2, p2mode)
        out1index = param_index(3, 0) #writing is never in immediate mode
        input_list[out1index] = op(input_list[in1index], input_list[in2index])
        index_increment(4)

    def opcode3(input1):
        out1index = param_index(1, 0)
        input_list[out1index] = input1
        index_increment(2)

    def opcode4():
        out1index = param_index(1, 0)
        print(input_list[out1index])
        index_increment(2)

    def jump_if(boolean):
        param1 = input_list[param_index(1, p1mode)]
        if bool(param1) == boolean:
            param2 = input_list[param_index(2, 0)]
            print(param2)
            nonlocal index
            index = param2
        else:
            index_increment(3)

    def compare(comparison):
        param1 = input_list[param_index(1, p1mode)]
        param2 = input_list[param_index(2, p2mode)]
        param3 = input_list[param_index(3, p3mode)]
        if comparison(param1, param2):
            write = 1
        else:
            write = 0
        input_list[param3] = write
        if index != param3:
            index_increment(4)

    running = True
    index = starting_index
    while running and index < (len(input_list) - 1):
        [opcode, p1mode, p2mode, p3mode] = decode_instruction(input_list[index])
        if opcode == 1:
            add_mul(add)
        elif opcode == 2:
            add_mul(mul)
        elif opcode == 3:
            opcode3(sys_id)
        elif opcode == 4:
            opcode4()
        elif opcode == 5:
            jump_if(True)
        elif opcode == 6:
            jump_if(False)
        elif opcode == 7:
            compare(lt)
        elif opcode == 8:
            compare(eq)
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
