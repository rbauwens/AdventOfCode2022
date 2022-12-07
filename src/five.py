import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 514

def process(array):
    start = []
    instructions = []
    inc = 0
    for line in array:
        if line != "":
            start.append(line)
            inc = inc + 1
        else:
            break
    num_columns = int(start[-1].strip()[-1])
    start = start[:-1]
    instructions = array[inc+1:]
    # print(start)
    # print(num_columns)
    # print(instructions)
    return [start, num_columns, instructions]
    
def get_columns(rows, num_columns):
    columns = []
    for col in range(num_columns):
        new_col = []
        for row in range(len(rows)):
            char = rows[row][((4*col)+1)]
            if char != ' ':
                new_col.append(char)
        # print(new_col)
        columns.append(new_col)
    return columns




def part_one(array):
  [rows, num_columns, instructions] = process(array)
  columns = get_columns(rows, num_columns)
  list = []
  for line in instructions:
    move = int(line.split("move ")[1].split(" ")[0])
    fro = int(line.split("from ")[1].split(" to ")[0])
    to = int(line.split("from ")[1].split(" to ")[1])
    # print(move, fro, to)
    # print(columns[0])
    # print(columns[1])
    # print(columns[2])
    for i in range(move):
        columns[to-1].insert(0, columns[fro-1][0])
        columns[fro-1].pop(0)
    #     print(columns[0])
    #     print(columns[1])
    #     print(columns[2])
    # print("#############")

  answer = ''
  for i in range(num_columns):
    answer = answer + columns[i][0]
#   print(answer)
  return answer


def part_two(array):
  [rows, num_columns, instructions] = process(array)
  columns = get_columns(rows, num_columns)
  list = []
  for line in instructions:
    move = int(line.split("move ")[1].split(" ")[0])
    fro = int(line.split("from ")[1].split(" to ")[0])
    to = int(line.split("from ")[1].split(" to ")[1])
    # print(move, fro, to)
    # print(columns[0])
    # print(columns[1])
    # print(columns[2])
    for i in range(move):
        columns[to-1].insert(0, columns[fro-1][move-(i+1)])
        columns[fro-1].pop(move-(i+1))
    # print(columns[0])
    # print(columns[1])
    # print(columns[2])
    # print("#############")

  answer = ''
  for i in range(num_columns):
    answer = answer + columns[i][0]
#   print(answer)
  return answer





test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("five", EXPECTED_LINES)

print(part_one(input))
print("###########################")
print(part_two(test_input_array))
print(part_two(input))

