#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 06 Part 2/buffer_output.txt'
header_check = ()
unique_check = 0
i = 0
x = 1

#this is to read the data buffer into a variable
with open(file_to_use, 'r') as file:
    data_buffer = file.read()

#this is to check the character against the buffer
while i < len(data_buffer):
    header_check = data_buffer[i:(i + 14)]
    for char in header_check:
        char_count = header_check.count(char)
        unique_check += char_count
        x += 1
        if x == 14:
            if unique_check == 14:
                print(i + 14)
                break
            else:
                unique_check = 0
                x = 0
    i += 1
