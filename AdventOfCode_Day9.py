# Part I
import copy


file = open("input_day9.txt", 'r')
lines = file.readlines()

head_pos = [0, 0]
tail_pos_history = [[0, 0]]

for line in lines:
    direction = line[0]
    steps = int(line[2:-1])

    for step in range(steps):
        # Move head
        if direction == 'U':
            head_pos[1] += 1
        elif direction == 'D':
            head_pos[1] -= 1
        elif direction == 'R':
            head_pos[0] += 1
        elif direction == 'L':
            head_pos[0] -= 1
        else:
            print("Something went wrong.")

        # Move tail
        # H H H H H
        # H       H
        # H   T   H
        # H       H
        # H H H H H
        tail_pos = tail_pos_history[-1].copy()
        if head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] + 2:
            tail_pos[0] -= 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] + 2:
            tail_pos[0] -= 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] + 2:
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] + 2:
            tail_pos[0] += 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] + 2:
            tail_pos[0] += 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] + 1:
            tail_pos[0] -= 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] + 1:
            tail_pos[0] += 1
            tail_pos[1] += 1
        elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1]:
            tail_pos[0] -= 1
        elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1]:
            tail_pos[0] += 1
        elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] - 1:
            tail_pos[0] -= 1
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] - 1:
            tail_pos[0] += 1
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] - 2:
            tail_pos[0] -= 1
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] - 2:
            tail_pos[0] -= 1
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] - 2:
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] - 2:
            tail_pos[0] += 1
            tail_pos[1] -= 1
        elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] - 2:
            tail_pos[0] += 1
            tail_pos[1] -= 1
        else:
            pass

        tail_pos_history.append(tail_pos)

tail_pos_hashable = []
for tail_pos in tail_pos_history:
    tail_pos_hashable.append(str(tail_pos))
unique_visited = len(set(tail_pos_hashable))

print(unique_visited)

file.close()

# Part II
import copy

def update_tail(tail_pos, head_pos):
    # Move tail
    # H H H H H
    # H       H
    # H   T   H
    # H       H
    # H H H H H
    if head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] + 2:
        tail_pos[0] -= 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] + 2:
        tail_pos[0] -= 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] + 2:
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] + 2:
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] + 2:
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] + 1:
        tail_pos[0] -= 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] + 1:
        tail_pos[0] += 1
        tail_pos[1] += 1
    elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1]:
        tail_pos[0] -= 1
    elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1]:
        tail_pos[0] += 1
    elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] - 1:
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] - 1:
        tail_pos[0] += 1
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] - 2:
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] - 2:
        tail_pos[0] -= 1
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1] - 2:
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] - 2:
        tail_pos[0] += 1
        tail_pos[1] -= 1
    elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] - 2:
        tail_pos[0] += 1
        tail_pos[1] -= 1
    else:
        pass
    return tail_pos


file = open("input_day9.txt", 'r')
lines = file.readlines()

head_pos = [0, 0]
mid_pos = [[0, 0]] * 9
tail_pos_history = [[0, 0]]

for line in lines:
    direction = line[0]
    steps = int(line[2:-1])

    for step in range(steps):
        # Move head
        if direction == 'U':
            head_pos[1] += 1
        elif direction == 'D':
            head_pos[1] -= 1
        elif direction == 'R':
            head_pos[0] += 1
        elif direction == 'L':
            head_pos[0] -= 1
        else:
            print("Something went wrong.")

        for i, pos in enumerate(mid_pos):
            if i == 0:
               mid_pos[i] = update_tail(pos, head_pos).copy()
            else:
                mid_pos[i] = update_tail(pos, mid_pos[i-1]).copy()
            if i == 8:
                tail_pos_history.append(mid_pos[i])

tail_pos_hashable = []
for tail_pos in tail_pos_history:
    tail_pos_hashable.append(str(tail_pos))
unique_visited = len(set(tail_pos_hashable))

print(unique_visited)
