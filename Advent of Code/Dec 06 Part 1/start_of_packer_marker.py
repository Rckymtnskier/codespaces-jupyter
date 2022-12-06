#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 06 Part 1/buffer_output.txt'
header_check = ()
i = 0

#this is to read the data buffer into a variable
with open(file_to_use, 'r') as file:
    data_buffer = file.read()

#this is to check the character against the buffer
while i < len(data_buffer):
    header_check = data_buffer[i:(i + 4)]
    pos_one = header_check[0]
    pos_two = header_check[1]
    pos_three = header_check[2]
    pos_four = header_check[3]
    unique_check = header_check.count(pos_one) + header_check.count(pos_two) + header_check.count(pos_three) + header_check.count(pos_four)
    if unique_check == 4:
        print(i + 4)
        break
    else:
        i += 1
        header_check = ()
    