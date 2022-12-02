import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 2500


def part_one(array):
    scores = []
    
    for entry in array:
        total = 0
        [p1,p2] = entry.split(" ")
        #rock
        if p2 == "X":
            total = 1
            if p1 == "A":
                total = total + 3
            elif p1 == "C":
                total = total + 6
        # paper
        if p2 == "Y":
            total = 2
            #rock
            if p1 == "A":
                total = total + 6
            elif p1 == "B":
                total = total + 3
        #scissors
        if p2 == "Z":
            total = 3
            if p1 == "B":
                total = total + 6
            elif p1 == "C":
                total = total + 3
        scores.append(total)
    # print(scores)
    return sum(scores)

        
def part_two(array):
    
    new_array = []
    for entry in array:
        [p1,p2] = entry.split(" ")
        if(p2 == "Y"):
            if p1 == "A":
                p2 = "X"
            elif p1 == "B":
                p2 = "Y"
            elif p1 == "C":
                p2 = "Z"
        elif (p2 == "X"):
            if p1 == "A":
                p2 = "Z"
            elif p1 == "B":
                p2 = "X"
            elif p1 == "C":
                p2 = "Y"
        elif (p2 == "Z"):
            if p1 == "A":
                p2 = "Y"
            elif p1 == "B":
                p2 = "Z"
            elif p1 == "C":
                p2 = "X"
        
        new_array.append("{} {}".format(p1, p2))
    return part_one(new_array)



test_input = """A Y
B X
C Z"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("two", EXPECTED_LINES)

print(part_one(input))
print("###########################")
print(part_two(test_input_array))
print(part_two(input))

