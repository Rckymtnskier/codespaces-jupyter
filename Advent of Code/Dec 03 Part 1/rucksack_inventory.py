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

#Setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 03 Part 1/inventory_list.txt'
pocket_one = []
pocket_two = []
inventory_list = []
value_list = []
i = 0


#reading the file line by line and splitting the lines into two lists to ease comparison
with open(file_to_use, 'r') as file:
    contents = file.readlines()
    for line in contents:
        #this is the mid point of each string
        split_point = (len(line) // 2)
        x = line.replace('\n', '')
        pocket_one.append(x[0:split_point])
        pocket_two.append(x[split_point:])

#this is to compare the items each of the pockets and to stop when a match is made and append the match to the inventory list    
while i < len(pocket_one):
    for char in pocket_one[i]:
        for letter in pocket_two[i]:
            if char == letter:
                inventory_list.append(char)
                break
        if char == letter:
            break        
    i += 1

#this is to convert the matched items to their priority values
for char in inventory_list:
    val = letters_to_values(char)
    value_list.append(val)

#this is to find the sum of the value list
print(sum(value_list))