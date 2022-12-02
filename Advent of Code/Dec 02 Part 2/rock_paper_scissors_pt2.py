#function to generate total score X
# A = ROCK     X = YOU LOSE 
# B = PAPER    Y = YOU DRAW
# C = SCISSORS Z = YOU WIN
def round_outcome(opponent, user):
    total_score = 0
    if opponent == 'A':
        if user == 'X':
            total_score = total_score + z 
            return total_score
        elif user == 'Y':
            total_score = total_score + x + draw
            return total_score
        elif user == 'Z':
            total_score = total_score + y + win 
            return total_score
    elif opponent == 'B':
        if user == 'X':
            total_score = total_score + x 
            return total_score
        elif user == 'Y':
            total_score = total_score + y + draw
            return total_score
        elif user == 'Z':
            total_score = total_score + z + win
            return total_score
    elif opponent == 'C':
        if user == 'X':
            total_score = total_score + y
            return total_score
        elif user == 'Y':
            total_score = total_score + z + draw 
            return total_score
        elif user == 'Z':
            total_score = total_score + x + win
            return total_score

#input file and defining score variables
file_to_use = '/workspaces/codespaces-jupyter/Advent of Code/Dec 02 Part 1/strategy_guide.txt'
x = 1 #ROCK VALUE
y = 2 #PAPER VALUE
z = 3 #SCISSORS VALUE
win = 6
draw = 3
final_score = 0


#opening file and creating an iterable
with open(file_to_use, 'r') as file:
    contents = file.readlines()

#iterating through contents of the file line by line and assinging values to variable for function above
for line in contents:
    round_score = round_outcome(line[0], line[2])
    final_score = final_score + round_score

#printing final score
print(final_score)