#function to append lists based upon what is on the readline
#def command_reader(command):
    #file_system = []
    #directory = []
#    if command[0] == 'cd' and command[1] != '..':
#        if command[0] not in directory:
#            directory.append(command[1])
#        elif command[0] in directory:
#            file_system.append(directory)
#            directory = []
#            directory.append(command[0])
#    elif command[0] == 'ls':
#        pass
#    elif command[0] != 'cd' and command[0] != 'dir' and command[0] != 'ls':
#        directory.append(int(command[0]))
#    elif command[0] == 'cd' and command[1] == '..':
#        file_system.append(directory)
#        directory = []
    
#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 07 Part 1/file_tree.txt'
file_system = []
directory = []
value_list = []
directory_value = []
sum_list = []
mem_cleared = []


#reading file
with open(file_to_use, 'r') as file:
    commands = file.readlines()

for command in commands:
    command = command.replace('$ ', '')
    command = command.split()
    #command_reader(command)
    if command[0] == 'cd' and command[1] != '..':
        if command[1] not in directory:
            directory.append(command[1])
        elif command[1] in directory:
            file_system.append(directory)
            directory = []
            directory.append(command[1])
    elif command[0] == 'ls':
        pass
    elif command[0] == 'dir':
        directory.append(command[1])
    elif command[0] != 'cd' and command[0] != 'dir' and command[0] != 'ls':
        directory.append(int(command[0]))
    elif command[0] == 'cd' and command[1] == '..':
        file_system.append(directory)
        directory = []

#this is to clean up the file system list
file_system = [list for list in file_system if list != []]

for list in file_system:
    print(list)

for line in file_system:
    directory_value = [ele for ele in line if type(ele)==int]
    value_list.append(directory_value)


