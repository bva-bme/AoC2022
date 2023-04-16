# Part I.

# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors

WINS = ["A Y", "B Z", "C X"]
TIES = ["A X", "B Y", "C Z"]
LOSS = ["A Z", "B X", "C Y"]

file = open("input_day2.txt", 'r')
lines = file.readlines()
total_score = 0
for line in lines:

    if line[2] == 'X':
        total_score += 1
    elif line[2] == 'Y':
        total_score += 2
    elif line[2] == 'Z':
        total_score += 3
    if line[0:3] in WINS:
        total_score += 6
    elif line[0:3] in TIES:
        total_score += 3
    elif line[0:3] in LOSS:
        total_score += 0

print(total_score)
file.close()

# Part II

# A for Rock
# B for Paper
# C for Scissors

# X for Lose
# Y for Draw
# Z for Win

WINS = ["A Z", "B Z", "C Z"]
TIES = ["A Y", "B Y", "C Y"]
LOSS = ["A X", "B X", "C X"]

ROCKS = ["A Y", "B X", "C Z"]
PAPERS = ["A Z", "B Y", "C X"]
SCISSORS = ["A X", "B Z", "C Y"]


file = open("input_day2.txt", 'r')
lines = file.readlines()
total_score = 0
for line in lines:

    if line[0:3] in ROCKS:
        total_score += 1
    elif line[0:3] in PAPERS:
        total_score += 2
    elif line[0:3] in SCISSORS:
        total_score += 3

    if line[0:3] in WINS:
        total_score += 6
    elif line[0:3] in TIES:
        total_score += 3
    elif line[0:3] in LOSS:
        total_score += 0

print(total_score)
file.close()
