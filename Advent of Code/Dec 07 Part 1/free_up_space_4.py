#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 07 Part 1/file_tree.txt'
file_system = {}
directory = []

#reading file
with open(file_to_use, 'r') as file:
    commands = file.readlines()

for line in commands:
    line = line.replace('$ ', '')
    line = line.split()
    if line[0] == 'cd' and line[1] != '..':
        dir_name = line[1]
    elif line[0] == 'ls':
        pass
    elif line[0] == 'dir':
        