import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 2262


def part_one(array):
    
  new_max = 0
  total = 0
  for entry in array:
    if entry != '':
      total = total + entry
    if entry == '':
      if total > new_max:
        new_max = total
      total = 0
  return new_max

        

def part_two(array):
    
  all_list = []
  total = 0
  for entry in array:
    if entry != '':
      total = total + entry
    if entry == '':
      all_list.append(total)
      total = 0
  all_list.append(total)
  total = 0
  # print(all_list)
  all_list.sort(reverse=True)
  return (all_list[0] + all_list[1] + all_list[2])


test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
test_input_array = test_input.split("\n")

for i in range(len(test_input_array)):
  if test_input_array[i] != '':
    test_input_array[i] = int(test_input_array[i])

print(part_one(test_input_array))

input = utils.get_instructions("one", EXPECTED_LINES)
for i in range(len(input)):
  if input[i] != '':
    input[i] = int(input[i])

print(part_one(input))

print(part_two(test_input_array))
print(part_two(input))
