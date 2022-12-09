import os
import sys
import math
sys.path.append(os.path.dirname(__file__))
import utils


EXPECTED_LINES = 991

def compute_dirsize(key):
  sum = 0
  for file in key:
    sum = sum + int(file[0])
  return sum


def part_one(array):
  dir_dict = dict()
  dir_path = ["/"]
  # current_folder_contents = []
  ls_active = False
  for line in array:

    # new command
    if line[0] == "$":
      ls_active = False
      command  = line.split("$ ")[1]
      # print(command)
      # change directory
      if "cd" in command:
        new_dir = command.split("cd ")[1]
        if new_dir == "/":
          dir_path = ["/"]
        elif new_dir == "..":
          dir_path.pop(-1)
        else:
          dir_path.append(new_dir)
        # print("new cwd: {}".format(dir_path))
      # ls
      elif "ls" in command:
        # need to capure lines until next command
        ls_active = True
        dir_dict[tuple(dir_path)] = []
        # current_folder_contents = []
    elif ls_active:
      if "dir" in line:
        new_folder = dir_path.copy()
        new_folder.append(line.split("dir ")[1])
        dir_dict[tuple(new_folder)] = []
      else:
        dir_dict[tuple(dir_path)].append(line.split(" "))
  
  
  # print(dir_dict)
  dir_sizes = dict()
  # print(dir_dict.keys())
  for key in dir_dict.keys():
      dir_sizes[key] = compute_dirsize(dir_dict[key])
  
  # print(dir_sizes)
  max = 0
  for key in dir_dict.keys():
    if len(key) > max:
      max = len(key)
  # print(max)
  while max > 1:
    tmp = dir_dict.copy()
    for key in dir_dict.keys():
      if len(key) == max:
        parent_dir = list(key).copy()
        parent_dir.pop(-1)
        parent_dir = tuple(parent_dir)
        dir_sizes[parent_dir] = dir_sizes[parent_dir] + dir_sizes[key]
        tmp.pop(key)
    max = max - 1
    dir_dict = tmp

  # print(dir_sizes[('/',)])
  # print(dir_sizes)
  result_sum = 0
  for key in dir_sizes.keys():
    if dir_sizes[key] <= 100000:
      result_sum = result_sum + dir_sizes[key]
  return result_sum
  

def part_two(array):
  dir_dict = dict()
  dir_path = ["/"]
  # current_folder_contents = []
  ls_active = False
  for line in array:

    # new command
    if line[0] == "$":
      ls_active = False
      command  = line.split("$ ")[1]
      # print(command)
      # change directory
      if "cd" in command:
        new_dir = command.split("cd ")[1]
        if new_dir == "/":
          dir_path = ["/"]
        elif new_dir == "..":
          dir_path.pop(-1)
        else:
          dir_path.append(new_dir)
        # print("new cwd: {}".format(dir_path))
      # ls
      elif "ls" in command:
        # need to capure lines until next command
        ls_active = True
        dir_dict[tuple(dir_path)] = []
        # current_folder_contents = []
    elif ls_active:
      if "dir" in line:
        new_folder = dir_path.copy()
        new_folder.append(line.split("dir ")[1])
        dir_dict[tuple(new_folder)] = []
      else:
        dir_dict[tuple(dir_path)].append(line.split(" "))
  
  
  # print(dir_dict)
  dir_sizes = dict()
  # print(dir_dict.keys())
  for key in dir_dict.keys():
      dir_sizes[key] = compute_dirsize(dir_dict[key])
  
  # print(dir_sizes)
  max = 0
  for key in dir_dict.keys():
    if len(key) > max:
      max = len(key)
  # print(max)
  while max > 1:
    tmp = dir_dict.copy()
    for key in dir_dict.keys():
      if len(key) == max:
        parent_dir = list(key).copy()
        parent_dir.pop(-1)
        parent_dir = tuple(parent_dir)
        dir_sizes[parent_dir] = dir_sizes[parent_dir] + dir_sizes[key]
        tmp.pop(key)
    max = max - 1
    dir_dict = tmp

  print(dir_sizes[('/',)])
  space_available = 70000000 - int(dir_sizes[('/',)])
  space_required = 30000000 - space_available
  print("space available: {}".format(space_available))
  print("space required: {}".format(space_required))
  # print(dir_sizes)
  result_sum = 0
  possibles =  []
  for key in dir_sizes.keys():
    if dir_sizes[key] >= space_required:
      possibles.append(key)
  print("len(possibles): {}".format(len(possibles)))      
  min = possibles[0]
  for dir in possibles:
    if dir_sizes[dir] < dir_sizes[min]:
      min = dir
  # print(min)
  print("-----------------")
  return dir_sizes[min]



test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
test_input_array = test_input.split("\n")

print(part_one(test_input_array))

input = utils.get_instructions("seven", EXPECTED_LINES)

print(part_one(input))

print("###########################")
print(part_two(test_input_array))
print(part_two(input))

# 43636666 too high