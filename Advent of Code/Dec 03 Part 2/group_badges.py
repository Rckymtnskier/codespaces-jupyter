#defining function to convert letters to priority values
def letters_to_values(letter):
    value_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28,
        'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
        'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
        'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }

    value = value_dict[letter]
    return value

#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 03 Part 2/inventory_list.txt'
elf_group_list = []
sub_group_list = []
badge_list = []
value_list = []
i = 0

#this is to read the inventory list
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#this is to split the elves into groups by iterating through the contents object
for item in contents:
    x = item.replace('\n', '')
    sub_group_list.append(x)
    i += 1
    #print(sub_group_list)
    if i == 3:
        elf_group_list.append(sub_group_list)
        i = 0
        sub_group_list = []

#this finds the matching letter for each group
while i < len(elf_group_list):
    for char in elf_group_list[i][0]:
        z = char
        if z in elf_group_list[i][1] and z in elf_group_list[i][2]:
            badge_list.append(z)
            break
    i += 1

#this is to convert the matched items to their priority values
for char in badge_list:
    val = letters_to_values(char)
    value_list.append(val)


#this is to find the sum of the value list
print(sum(value_list))