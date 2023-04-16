# Part I

file = open("input_day6.txt", 'r')
lines = file.readlines()

buf = 'AAAA'
i = 1

for char in lines[0]:
    buf += char
    buf = buf[1:]

    start_flag = True
    for j, c1 in enumerate(buf):
        for k, c2 in enumerate(buf):
            if j == k:
                continue
            if c1 == c2:
                start_flag = False

    if i >= 4 and start_flag:
        break
    i += 1

print(i)
file.close()

# Part II

file = open("input_day6.txt", 'r')
lines = file.readlines()

buf = 'AAAAAAAAAAAAAA'
i = 1

for char in lines[0]:
    buf += char
    buf = buf[1:]

    start_flag = True
    for j, c1 in enumerate(buf):
        for k, c2 in enumerate(buf):
            if j == k:
                continue
            if c1 == c2:
                start_flag = False

    if i >= 14 and start_flag:
        break
    i += 1

print(i)
file.close()
