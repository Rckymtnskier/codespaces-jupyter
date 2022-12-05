#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 04 Part 1/pairings.txt'
pairing_list = []

#read the pairings list
with open(file_to_use, 'r') as file:
    contents = file.readlines()

for pair in contents:
    x = pair.replace('\n', '')
    y = x.split(',')
    pairing_list.append(y)

for pair in pairing_list:
    for set in pair:
        