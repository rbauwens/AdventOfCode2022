import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 1000



def part_one(array):
    count = 0
    for entry in array:
        [a, b] = entry.split(",")
        a1 = int((a.split("-")[0]))
        a2 = int((a.split("-")[1]))
        b1 = int((b.split("-")[0]))
        b2 = int((b.split("-")[1]))
        a_list = list(range(a1, a2 + 1))
        b_list = list(range(b1, b2 + 1))
        set_a = set(a_list)
        set_b = set(b_list)
        
        if ((set_a.issubset(set_b)) or (set_b.issubset(set_a))):
            # print(set(a_list).intersection(set(b_list)))
            count = count + 1
    return count

def part_two(array):
    count = 0
    for entry in array:
        [a, b] = entry.split(",")
        a1 = int((a.split("-")[0]))
        a2 = int((a.split("-")[1]))
        b1 = int((b.split("-")[0]))
        b2 = int((b.split("-")[1]))
        a_list = list(range(a1, a2 + 1))
        b_list = list(range(b1, b2 + 1))
        set_a = set(a_list)
        set_b = set(b_list)
        
        intersection = set(a_list).intersection(set(b_list))
        if len(intersection) > 0:
            count = count + 1
    return count


test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("four", EXPECTED_LINES)

print(part_one(input))
print("###########################")
print(part_two(test_input_array))
print(part_two(input))

