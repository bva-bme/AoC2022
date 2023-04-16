# Part I

file = open("input_day3.txt", 'r')
lines = file.readlines()

priority_list = []
for line in lines:
    line = line[:-1]
    half_len = int(len(line)/2)
    comp1 = line[0:half_len]
    comp2 = line[half_len:]

    duplicate_char = ''
    for c1 in comp1:
        for c2 in comp2:
            if c1 == c2:
                duplicate_char = c1
                print(c1)
                break
        else:
            continue
        break
    duplicate_char_ascii = ord(duplicate_char)
    if duplicate_char_ascii > 96:
        priority_list.append(duplicate_char_ascii - 96)
    else:
        priority_list.append(duplicate_char_ascii - 64 + 26)

print(sum(priority_list))
file.close()

# Part II

def find_common(line_buf):
    for c0 in line_buf[0]:
        for c1 in line_buf[1]:
            if c0 == c1:
                for c2 in line_buf[2]:
                    if c1 == c2:
                        return c1

file = open("input_day3.txt", 'r')
lines = file.readlines()
priority_list = []
line_buf = []
for line in lines:
    line = line[:-1]
    line_buf.append(line)
    if len(line_buf) == 3:
        duplicate_char = find_common(line_buf)

        duplicate_char_ascii = ord(duplicate_char)
        if duplicate_char_ascii > 96:
            priority_list.append(duplicate_char_ascii - 96)
        else:
            priority_list.append(duplicate_char_ascii - 64 + 26)

        line_buf = []

print(sum(priority_list))
file.close()

