# Part I

file = open("input_day5.txt", 'r')
lines = file.readlines()

n_cols = 9
crates = [ [] for _ in range(n_cols)]
for line in lines:
    if ' 1   2   3' in line:
        break
    for i in range(n_cols):
        if len(line) < i * 4 + 1:
            break
        if line[i * 4 + 1] != ' ':
            crates[i].append(line[i * 4 + 1])
for columns in crates:
    columns.reverse()

for line in lines:
    if 'move' not in line:
        continue
    line_split = line.split(' ')
    n_move = int(line_split[1])
    n_from = int(line_split[3]) - 1
    n_to = int(line_split[5]) - 1

    for i in range(n_move):
        to_move = crates[n_from][-1]
        crates[n_from].pop()
        crates[n_to].append(to_move)

result = ''

for column in crates:
    result += column[-1]
print(result)
file.close()


# Part II

file = open("input_day5.txt", 'r')
lines = file.readlines()

n_cols = 9
crates = [ [] for _ in range(n_cols)]
for line in lines:
    if ' 1   2   3' in line:
        break
    for i in range(n_cols):
        if len(line) < i * 4 + 1:
            break
        if line[i * 4 + 1] != ' ':
            crates[i].append(line[i * 4 + 1])
for columns in crates:
    columns.reverse()

for line in lines:
    if 'move' not in line:
        continue
    line_split = line.split(' ')
    n_move = int(line_split[1])
    n_from = int(line_split[3]) - 1
    n_to = int(line_split[5]) - 1

    moving = []
    for i in range(n_move):
        to_move = crates[n_from][-1]
        crates[n_from].pop()
        moving.append(to_move)
    moving.reverse()
    crates[n_to] += moving

result = ''

for column in crates:
    result += column[-1]
print(result)
file.close()