import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
from itertools import permutations, product


EXPECTED_LINES = 2000

def compute_distance(a, b):
  dist_a = pow(b[0] - a[0], 2)
  dist_b = pow(b[1] - a[1], 2)
  return int(math.sqrt(dist_a + dist_b))

def move_T(pos_T, pos_H):
  if pos_T[0] == pos_H[0]:
    # in same vertical line
    # print("vertical")
    if pos_H[1] == pos_T[1] + 2:
      return [pos_T[0], pos_T[1] + 1]
    elif pos_H[1] == pos_T[1] - 2:
      return [pos_T[0], pos_T[1] - 1]
    else:
      print("don't know what i'm doing")
  elif pos_T[1] == pos_H[1]:
    # in same horiz line
    # print("horiz")
    if pos_H[0] == pos_T[0] + 2:
      return [pos_T[0] + 1, pos_T[1]]
    elif pos_H[0] == pos_T[0] - 2:
      return [pos_T[0] - 1, pos_T[1]]
    else:
      print("don't know what i'm doing")
  else:
    # print("diag")
    diff_x = pos_H[0] - pos_T[0]
    diff_y = pos_H[1] - pos_T[1]
    if (abs(diff_x) == 2) and abs(diff_y) == 2:
      pos_T[0] = int(pos_T[0] + (diff_x/2))
      pos_T[1] = int(pos_T[1] + (diff_y/2))
    elif abs(diff_x) == 2:
      pos_T[0] = int(pos_T[0] + (diff_x/2))
      pos_T[1] = pos_H[1]
    elif abs(diff_y) == 2:
      pos_T[0] = pos_H[0]
      pos_T[1] = int(pos_T[1] + (diff_y/2))
    return pos_T

  return pos_T

def part_one(array):
  all_T = []
  pos_T = [0, 0]
  pos_H = [0, 0]
  all_T.append(pos_T)
  
  

  for line in array:
    # print("##########")
    # print(line)
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if direction == 'R':
      for step in range(distance):
        pos_H[0] = pos_H[0] + 1
        dist = compute_distance(pos_T, pos_H)
        if dist > 1:
          pos_T = move_T(pos_T, pos_H)
        # print("pos_H: {}", pos_H)
        # print("pos_T: {}", pos_T)
        if pos_T not in all_T:
          all_T.append(pos_T.copy())
    elif direction == 'L':
      for step in range(distance):
        pos_H[0] = pos_H[0] - 1
        dist = compute_distance(pos_T, pos_H)
        if dist > 1:
          pos_T = move_T(pos_T, pos_H)
        # print("pos_H: {}", pos_H)
        # print("pos_T: {}", pos_T)
        if pos_T not in all_T:
          all_T.append(pos_T.copy())
    elif direction == 'U':
      for step in range(distance):
        pos_H[1] = pos_H[1] + 1
        dist = compute_distance(pos_T, pos_H)
        if dist > 1:
          pos_T = move_T(pos_T, pos_H)
        # print("pos_H: {}", pos_H)
        # print("pos_T: {}", pos_T)
        if pos_T not in all_T:
          all_T.append(pos_T.copy())
    elif direction == 'D':
      for step in range(distance):
        pos_H[1] = pos_H[1] - 1
        dist = compute_distance(pos_T, pos_H)
        if dist > 1:
          pos_T = move_T(pos_T, pos_H)
        # print("pos_H: {}", pos_H)
        # print("pos_T: {}", pos_T)
        if pos_T not in all_T:
          all_T.append(pos_T.copy())

  # print(all_T)
  return len(all_T)


def part_two(array):
  all_T = []
  Tail = []
  for _ in range(10):
    Tail.append([0,0])
  # print(len(Tail))
  
  pos_H = [0, 0]
  all_T.append(Tail[9].copy())
  
  

  for line in array:
    # print("----------------")
    # print(line)
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if direction == 'R':
      for step in range(distance):
        # pos_H[0] = pos_H[0] + 1
        Tail[0][0] = Tail[0][0] + 1
        for i in range(1, 10):
          dist = compute_distance(Tail[i], Tail[i-1])
          if dist > 1:
            Tail[i] = move_T(Tail[i], Tail[i-1])
          # print("pos_H: {}", pos_H)
          # print("pos_T: {}", pos_T)
        # print(Tail)
        if Tail[9] not in all_T:
          all_T.append(Tail[9].copy())
    elif direction == 'L':
      for step in range(distance):
        # pos_H[0] = pos_H[0] - 1
        Tail[0][0] = Tail[0][0] - 1
        for i in range(1, 10):
          dist = compute_distance(Tail[i], Tail[i-1])
          if dist > 1:
            Tail[i] = move_T(Tail[i], Tail[i-1])
          # print("pos_H: {}", pos_H)
          # print("pos_T: {}", pos_T)
        # print(Tail)
        if Tail[9] not in all_T:
          all_T.append(Tail[9].copy())
    elif direction == 'U':
      for step in range(distance):
        # pos_H[1] = pos_H[1] + 1
        Tail[0][1] = Tail[0][1] + 1
        for i in range(1, 10):
          dist = compute_distance(Tail[i], Tail[i-1])
          if dist > 1:
            Tail[i] = move_T(Tail[i], Tail[i-1])
          # print("pos_H: {}", pos_H)
          # print("pos_T: {}", pos_T)
        # print(Tail)
        if Tail[9] not in all_T:
          all_T.append(Tail[9].copy())
    elif direction == 'D':
      for step in range(distance):
        # pos_H[1] = pos_H[1] - 1
        Tail[0][1] = Tail[0][1] - 1
        for i in range(1, 10):
          dist = compute_distance(Tail[i], Tail[i-1])
          if dist > 1:
            Tail[i] = move_T(Tail[i], Tail[i-1])
          # print("pos_H: {}", pos_H)
          # print("pos_T: {}", pos_T)
        # print(Tail)
        if Tail[9] not in all_T:
          all_T.append(Tail[9].copy())
    # print(Tail)

  # print("")
  # print(all_T)
  return len(all_T)
  
        
    



      


test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
test_input_array = test_input.split("\n")
test_input_array2 = test_input2.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("nine", EXPECTED_LINES)

# print(part_one(input))

print("###########################")
print(part_two(test_input_array))
print(part_two(test_input_array2))
print(part_two(input))

