def create_grid(lines):
    occupancy_grid = []

    for line in lines:
        str_coord_list = line[:-1].split(' -> ')
        for i in range(len(str_coord_list)-1):
            str_x1, str_y1 = str_coord_list[i].split(',')
            str_x2, str_y2 = str_coord_list[i+1].split(',')
            x1 = int(str_x1)
            x2 = int(str_x2)
            y1 = int(str_y1)
            y2 = int(str_y2)

            occupancy_grid.append([x1, y1])
            occupancy_grid.append([x2, y2])

            if x1 == x2:
                if y2 > y1:
                    for j in range(y2-y1):
                        if j == 0:
                            pass
                        else:
                            occupancy_grid.append([x1, y1+j])
                elif y2 < y1:
                    for j in range(y1-y2):
                        if j == 0:
                            pass
                        else:
                            occupancy_grid.append([x1, y2+j])
            else:
                if x2 > x1:
                    for j in range(x2-x1):
                        if j == 0:
                            pass
                        else:
                            occupancy_grid.append([x1+j, y1])
                elif x2 < x1:
                    for j in range(x1-x2):
                        if j == 0:
                            pass
                        else:
                            occupancy_grid.append([x2+j, y1])
    return occupancy_grid


def drop_sand(occupancy_grid):
    x = 500
    y = 0
    fell_ctr = 0
    while True:
        if fell_ctr > 1000:
            return occupancy_grid, True
        if [x, y+1] not in occupancy_grid:
            y += 1
            fell_ctr += 1
            continue
        elif [x-1, y+1] not in occupancy_grid:
            x -= 1
            y += 1
            fell_ctr += 1
            continue
        elif [x+1, y+1] not in occupancy_grid:
            x += 1
            y += 1
            fell_ctr += 1
            continue
        else:
            occupancy_grid.append([x, y])
            if x == 500 and y == 0:
                return occupancy_grid, True
            else:
                return occupancy_grid, False


def append_floor(occupancy_grid):

    max_depth = 0
    for point in occupancy_grid:
        if point[1] > max_depth:
            max_depth = point[1]

    y = max_depth+2
    for x in range(1000):
        occupancy_grid.append([x, y])
    return occupancy_grid

# Part I

file = open("input_day14.txt", 'r')
lines = file.readlines()

grid = create_grid(lines)

drop = 0

while True:
    grid, done = drop_sand(grid)
    if done:
        break
    drop += 1

print(drop)


# Part II

grid = []
grid = create_grid(lines)
grid = append_floor(grid)

drop = 0

while True:
    grid, done = drop_sand(grid)
    drop += 1
    if done:
        break

print(drop)

file.close()