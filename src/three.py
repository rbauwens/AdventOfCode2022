import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 300

def get_value(common):
    if common.islower():
        return (ord(common) - ord("a") + 1)
    else:
        return (ord(common) - ord("A") + 1 + 26)
    

def part_one(array):
    sum = 0
    
    for entry in array:
        
        half = (len(entry))//2
        p1 = entry[0:half]
        p2 = entry[half:]
        common = utils.common_char(p1, p2)
        value = get_value(common)
        sum = sum + value
    return sum 

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def part_two(array):
    sum = 0
    for entry in chunks(array, 3):
        common = utils.common_char_three(entry[0], entry[1], entry[2])
        value = get_value(common)
        sum = sum + value
    return sum





test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("three", EXPECTED_LINES)

print(part_one(input))
print("###########################")
print(part_two(test_input_array))
print(part_two(input))

