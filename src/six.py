import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
from itertools import islice 


EXPECTED_LINES = 1


def gen(input, length):
  it = iter(input)
  result = tuple(islice(it, length))
  if len(result) == length:
    yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result



def part_one(input):
  count = 3
  length = 4
  for entry in gen(input, length):
    count = count + 1
    # print(entry)
    if len(entry) == len(set(entry)):
      return(count)

def part_two(input):
  count = 13
  length = 14
  for entry in gen(input, length):
    count = count + 1
    # print(entry)
    if len(entry) == len(set(entry)):
      return(count)




input_one = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

print(part_one(input_one))

input = utils.get_instructions("six", EXPECTED_LINES)

print(part_one(input[0]))
print("###########################")
print(part_two(input[0]))

