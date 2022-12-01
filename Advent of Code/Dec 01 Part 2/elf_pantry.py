#this references the local file to use as input and creates the requiste lists for the script
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 01 Part 2/data_input.txt'
data_list = []
elf_calories = []
total_calories_per_elf = []

#this opens the file and creates an iterable item of the contents
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#this was for consistancy checking to see how many elves there were
elf_count = contents.count('\n')

#this converts the calorie strings to integers and then sorts them into nested lists within the main list by using '\n' as the delimiter
for unit in contents:
    if unit != '\n':
        num = int(unit)
        elf_calories.append(num)
    elif unit == '\n':
        data_list.append(elf_calories)
        elf_calories = []

#this sums up the calories each elf is carrying
for elf in data_list:
    elf_sum = sum(elf)
    total_calories_per_elf.append(elf_sum)

#this finds the max value of calories being carried by an elf
max_cal = max(total_calories_per_elf)

#this prints the maximum amount of calories an elf is holding, and then finds which elf it is
print(max_cal)
print(total_calories_per_elf.index(max_cal))

#this sorts the list 
total_calories_per_elf.sort()

#this finds the top three elves carrying the most calories and sums the total of their calories carried
top_three = total_calories_per_elf[-1] + total_calories_per_elf[-2] + total_calories_per_elf[-3]
print(top_three)