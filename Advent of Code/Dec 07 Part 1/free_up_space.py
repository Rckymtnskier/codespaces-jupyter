#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 07 Part 1/file_tree.txt'
file_system = []
directory = []

#function to append lists based upon what is on the readline
#def line_reader(read_line):
   
    
      
#reading file
with open(file_to_use, 'r') as file:
    commands = file.readlines()

#read through file line by line and output the results to a list of lists
for line in commands:
    x = line.replace('$ ', '')
    read_line = x.split()
    #line_reader(x)
    if read_line[0] == 'cd' and read_line[1] != '..':
        file_system.append(directory)
        directory = []
        directory.append(f'name:{read_line[1]}')
    if read_line[0] == 'ls':
        pass
    if read_line[0] == 'dir':
        directory.append(read_line[1])
    if read_line[0] != 'cd' and read_line[0] != 'dir' and read_line[0] != 'ls':
        directory.append(int(read_line[0]))
    if read_line[0] == 'cd' and read_line[1] == '..':
        file_system.append(directory)
        directory = []
    
#this is to clean up the file system list
file_system = [list for list in file_system if list != []]

for list in file_system:
    print(list)
