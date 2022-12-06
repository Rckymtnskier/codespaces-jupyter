#function to find overlapping pairs
def overlapping_pairs(pair_one, pair_two):
    sp_one = len(pair_one) // 2
    sp_two = len(pair_two) // 2
    low_one = int(pair_one[:sp_one])
    high_one = int(pair_one[sp_one:])
    low_two = int(pair_two[:sp_two])
    high_two = int(pair_two[sp_two:])

    if low_one >= low_two and high_one <= high_two:
        return 1
    elif low_two >= low_one and high_two <= high_one:
        return 1
    else:
        return 0


#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 04 Part 1/pairings.txt'
pairing_list = []
matched_list = []

#read the pairings list
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#this is to strip down the strings and put them in a list
for pair in contents:
    x = pair.replace('\n', '')
    x = x.replace('-', '')
    y = x.split(',')
    pairing_list.append(y)

#this is a list comprehension to change the strings to integers
#integer_pairs = [[int(group) for group in pair] for pair in pairing_list]

#this is to run the function to find overlapping pairs
for pair in pairing_list:
    x = overlapping_pairs(pair[0], pair[1])
    matched_list.append(x)

#this is to find the total of overlapping pairs
print(sum(matched_list))