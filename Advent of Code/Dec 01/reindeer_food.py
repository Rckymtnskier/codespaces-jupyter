file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 01/data_input.txt'
data_list = []
elf_calories = []
total_calories_per_elf = []

with open(file_to_use, 'r') as file:
    contents = file.readlines()

elf_count = contents.count('\n')

for unit in contents:
    if unit != '\n':
        num = int(unit)
        elf_calories.append(num)
    elif unit == '\n':
        data_list.append(elf_calories)
        elf_calories = []

for elf in data_list:
    elf_sum = sum(elf)
    total_calories_per_elf.append(elf_sum)

max_cal = max(total_calories_per_elf)

print(max_cal)
print(total_calories_per_elf.index(max_cal))