#setting up variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 08 Part 1/tree_plot.txt'
tree_grid = []
tree_row = []
visible_row = []
visible_grid = []
line_sum = 0

#reading file
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#formatting data for use
for line in contents:
    line = line.replace('\n', '')
    for char in line:
        char = int(char)
        tree_row.append(char)
    tree_grid.append(tree_row)
    tree_row = []

rows = len(tree_grid)
columns = len(tree_grid[0])
mid_point = (rows // 2) + 1
x = 0
y = 0
current_max = 0



while y < rows:
    for char in tree_grid[y][:mid_point]:
        if char > current_max:
            visible_row.append('v')
            current_max = char
        elif char <= current_max:
            visible_row.append('.')
    visible_grid.append(visible_row)
    visible_row = []
    current_max = 0
    for char in tree_grid[y][mid_point::-1]:
        if char > current_max:
            visible_row.append('v')
            current_max = char
        elif char <= current_max:
            visible_row.append('.')
    visible_row.reverse()
    visible_grid[y].extend(visible_row)
    visible_row = []
    current_max = 0

    y += 1

x = 0
y = 0
current_max = 0

while x < columns:
    while y < rows:        
        if tree_grid[y][x] > current_max:
            current_max = tree_grid[y][x]
            if visible_grid[y][x] == '.':
                del visible_grid[y][x]
                visible_grid[y].insert(x,'v')
            y += 1
        elif tree_grid[y][x] <= current_max:
            y += 1
    x += 1
    current_max = 0







print(visible_grid)
for line in visible_grid:
    line_sum += line.count('v')

print(line_sum)
