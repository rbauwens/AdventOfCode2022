import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils
from itertools import permutations, product


EXPECTED_LINES = 99


def part_one(array):
  # print(array)
  across = len(array[0])
  down = len(array)
  # print(across, down)
  outer_trees = (2*across) + (2*(down - 2))
  # print(outer_trees)
  
  new_array = []
  for line in array:
    new_array.append(list(line))
  
  # print(new_array)
  trees = list(product(list(range(across)), list(range(down))))
  assert len(trees) == across * down
  inner_trees = 0
  for tree in trees:
    visible = False
    if (tree[0] == 0) or (tree[1] == 0) or (tree[0] == across-1) or (tree[1] == down-1):
      continue
    else:
      # across first
      height = new_array[tree[0]][tree[1]]
      # print("at ({}, {}) height is {}".format(tree[0], tree[1], height))
      tree_across  = tree[0]
      tree_down  = tree[1]
      
      # print(new_array[tree_across])
      
      # index_h = new_array[tree_across].index(height)
      index_h = tree_down
      across_line = new_array[tree_across].copy()

      #left
      max_l = max(list(across_line[:index_h]))
      max_r = max(list(across_line[index_h+1:]))
      # print(max_l, max_r)
      if (int(max_l) < int(height)) or (int(max_r) < int(height)):
        visible = True

      
      if visible == False:
        # continue to look at down
        down_list = []
        for i in range(down):
          down_list.append(new_array[i][tree[1]])
        # print(down_list)

        #left
        max_u = max(list(down_list[:int(tree[0])]))
        max_d = max(list(down_list[int(tree[0])+1:]))
        # print(max_u, max_d)
        if (int(max_u) < int(height)) or (int(max_d) < int(height)):
          visible = True


    if visible == True:
      inner_trees = inner_trees + 1
      # print("visible")
    # else:
      # print("not visible")
    # print("------------")
  # print(inner_trees)
  # print(outer_trees + inner_trees)
  return (outer_trees + inner_trees)


def part_two(array):
  max_scenic_score = 0
  # print(array)
  across = len(array[0])
  down = len(array)
  # print(across, down)
  outer_trees = (2*across) + (2*(down - 2))
  # print(outer_trees)
  
  new_array = []
  for line in array:
    new_array.append(list(line))
  
  # print(new_array)
  trees = list(product(list(range(across)), list(range(down))))
  assert len(trees) == across * down
  inner_trees = 0
  for tree in trees:
    visible = False
    if (tree[0] == 0) or (tree[1] == 0) or (tree[0] == across-1) or (tree[1] == down-1):
      continue
    else:
      # across first
      height = new_array[tree[0]][tree[1]]
      # print("at ({}, {}) height is {}".format(tree[0], tree[1], height))
      tree_across  = tree[0]
      tree_down  = tree[1]
      
      # print(new_array[tree_across])
      
      index_h = tree_down
      across_line = new_array[tree_across].copy()

      #left
      see = True
      see_l = 0
      x = 1
      while see == True and (index_h - x) >= 0:
        if (int(across_line[index_h - x])) < int(height):
          see_l = see_l + 1
        else:
          see_l = see_l + 1
          see= False
        x = x + 1

      #right
      see = True
      see_r = 0
      x = 1
      while see == True and (index_h + x) < across:
        if (int(across_line[index_h + x])) < int(height):
          see_r = see_r + 1
        else:
          see_r = see_r + 1
          see= False
        x = x + 1

      
      # continue to look at down
      down_list = []
      for i in range(down):
        down_list.append(new_array[i][tree[1]])
      # print(down_list)

      #up
      index_h = tree[0]
      see = True
      see_u = 0
      x = 1
      while see == True and (index_h - x) >= 0:
        if (int(down_list[index_h - x])) < int(height):
          see_u = see_u + 1
        else:
          see_u = see_u + 1
          see= False
        x = x + 1

      #down
      index_h = tree[0]
      see = True
      see_d = 0
      x = 1
      while see == True and (index_h + x) < down:
        if (int(down_list[index_h + x])) < int(height):
          see_d = see_d + 1
        else:
          see_d = see_d + 1
          see= False
        x = x + 1

    scenic_score = see_l*see_r*see_u*see_d
    # print(scenic_score)
    if scenic_score > max_scenic_score:
      max_scenic_score = scenic_score


  return max_scenic_score
      


test_input = """30373
25512
65332
33549
35390"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("eight", EXPECTED_LINES)

print(part_one(input))

print("###########################")
print(part_two(test_input_array))
print(part_two(input))

