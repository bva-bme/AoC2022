# Part I

file = open("input_day10.txt", 'r')
lines = file.readlines()

cyc_to_eval = [20, 60, 100, 140, 180, 220]
val_to_eval = []

X = 1
cyc = 0

for line in lines:
    if line[0:4] == 'noop':
        cyc += 1
        if cyc in cyc_to_eval:
            val_to_eval.append(X)
    elif line[0:4] == 'addx':
        cyc += 2
        if cyc in cyc_to_eval or cyc-1 in cyc_to_eval:
            val_to_eval.append(X)
        X += int(line[5:-1])

power = 0
for c, v in zip(cyc_to_eval, val_to_eval):
    power += c*v

print(power)


# Part II

screen = [[' '] * 40 for i in range(6)]

X = 1
cyc = 0
cyc_arr = [0]
x_arr = [1]

for line in lines:
    if line[0:4] == 'noop':
        cyc += 1
        cyc_arr.append(cyc)
        x_arr.append(X)

    elif line[0:4] == 'addx':
        cyc += 1
        cyc_arr.append(cyc)
        x_arr.append(X)
        cyc += 1
        cyc_arr.append(cyc)
        X += int(line[5:-1])
        x_arr.append(X)

x_arr_reshaped = [[x_arr[j*40 + i] for i in range(40)] for j in range(6)]

for i in range(6):
    for j in range(40):
        if j == x_arr_reshaped[i][j]:
            screen[i][j] = "#"
        elif j == x_arr_reshaped[i][j] - 1:
            screen[i][j] = "#"
        elif j == x_arr_reshaped[i][j] + 1:
            screen[i][j] = "#"
    print(''.join(screen[i]))

file.close()