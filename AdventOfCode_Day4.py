# Part I

import re

file = open("input_day4.txt", 'r')
lines = file.readlines()

contained = 0
for line in lines:
    line_split = re.split('-|,', line[:-1])
    if int(line_split[1]) >= int(line_split[3]) and int(line_split[0]) <= int(line_split[2]) or \
        int(line_split[3]) >= int(line_split[1]) and int(line_split[2]) <= int(line_split[0]):
            contained += 1

print(contained)
file.close()

# Part II

file = open("input_day4.txt", 'r')
lines = file.readlines()

overlap = 0
for line in lines:
    line_split = re.split('-|,', line[:-1])
    range1 = set([*range(int(line_split[0]), int(line_split[1])+1, 1)])
    range2 = set([*range(int(line_split[2]), int(line_split[3])+1, 1)])
    if range1 & range2:
        overlap += 1

print(overlap)
file.close()
