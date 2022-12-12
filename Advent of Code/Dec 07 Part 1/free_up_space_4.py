#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 07 Part 1/file_tree.txt'
file_system = {}
directory = {}

#reading file
with open(file_to_use, 'r') as file:
    commands = file.readlines()

#for line in commands:
#    line = line.replace('$ ', '')
#    line = line.split()
#    if line[0] == 'cd' and line[1] != '..':
#        file_system.update(directory)
#        dir_name = line[1]
#    elif line[0] == 'ls':
#        pass
#    elif line[0] == 'dir':
#        directory.update({dir_name: line[1]})
#    elif line[0] != 'cd' and line[0] != 'dir' and line[0] != 'ls':
#        directory.update({dir_name: line[0]})
#    elif line[0] == 'cd' and line[1] == '..':
#        pass

dir_name = '/'
sub_dir = 'asdf'
file = 12345
directory.update({'dir':sub_dir})
directory.update({'size':file})
file_system.update({dir_name:directory})

print(file_system)