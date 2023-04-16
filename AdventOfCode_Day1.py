cal_data = open('input_day1.txt', 'r')

cal_max = 0
cal_this = 0
e_ctr = 0

cal_buf = [0] * 3

while True:

    # Get next line from file
    line = cal_data.readline()
    if line == '\n':
        e_ctr += 1
        if cal_buf[0] < cal_this:
            cal_max = cal_this
            cal_buf.pop(0)
            cal_buf.append(cal_max)
            cal_buf.sort()
        cal_this = 0
    elif line == '':
        break
    else:
        cal_this += int(line)


print(sum(cal_buf))
print(e_ctr, cal_max)

cal_data.close()