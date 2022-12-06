#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 05 Part 2/instructions.txt'
pile_list  = [
    ['B', 'S', 'V', 'Z', 'G', 'P', 'W'], 
    ['J', 'V', 'B', 'C', 'Z', 'F'],
    ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
    ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
    ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
    ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
    ['L', 'G', 'C', 'Z', 'V'],
    ['N', 'L', 'G'],
    ['J', 'F', 'H', 'C']]

instruction_list = []

moved_item_list = []

#reading instructions
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#this is to format the contents for use
for line in contents:
    x = line.replace('move', '')
    x = x.replace('from', '')
    x = x.replace('to', '')
    x = x.replace('\n', '')
    x = x.replace(' ', '')
    instruction_list.append(x)

#this is to move the crates around, pop, and append the lists
for line in instruction_list:
    num_items = int(line[:-2]) * -1
    from_pile = int(line[-2]) - 1
    to_pile = int(line[-1]) - 1
#this takes the end of a list and copies it to the moved item list, then deletes what was coppied
#then extends the sub-list with the moved item list, and then empties the moved item list
    moved_item_list = pile_list[from_pile][num_items:]
    del pile_list[from_pile][num_items:]
    pile_list[to_pile].extend(moved_item_list)
    moved_item_list = []


#this is to print the results    
for line in pile_list:
    print(line[-1], end='')
print()