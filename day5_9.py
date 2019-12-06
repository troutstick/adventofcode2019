from operator import add, mul, sub

#####################
# Day 5
#####################

def intcode(input_list):
    """Takes in an input list and mutates it accordingly"""
    def give_param(param_num, mode, index):
        index = input_list[index+param_num]
        if mode:
            param = index
        else:
            param = input_list[index]
        return param


    def intcode_helper(index, mode=0):
        """Runs one iteration of the intcode program"""

        def add_mul(op):
            input1 = give_param(1, p1mode, index)
            input2 = give_param(2, p2mode, index)
            output1 = give_param(3, p3mode, index)
            input_list[output1] = op(input_list[input1], input_list[input2])

        instructions = decode_instruction(input_list[index])
        opcode = instructions[0]
        p1mode = instructions[1]
        p2mode = instructions[2]
        p3mode = instructions[3]
        if opcode == 1:
            op = add
        elif opcode == 2:
            op = mul
        elif opcode == 3:
        elif opcode == 99:
            raise IntcodeException
        else:
            print("you shouldn't see me")



        if p2mode:
            second_index = input_list[index+2]
        output_index = input_list[index+3]

        if

        input_list[output_index] = op(input_list[first_index], input_list[second_index])

    i = 0
    while i < (len(input_list) - 1):
        try:
            intcode_helper(i)
            i += 4
        except IntcodeException:
            break

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


class IntcodeException(Exception):
    pass
