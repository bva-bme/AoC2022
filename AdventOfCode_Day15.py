import time
import math

def calc_manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def get_data(lines):
    sensors = []
    beacons = []
    distances = []
    for line in lines:
        x_S = int(line[line.find('x=')+2:line.find(',')])
        y_S = int(line[line.find('y=')+2:line.find(':')])
        line2 = line[line.find('beacon'):]
        x_B = int(line2[line2.find('x=') + 2:line2.find(',')])
        y_B = int(line2[line2.find('y=') + 2:line2.find('\n')])

        dist = calc_manhattan_distance(x_S, y_S, x_B, y_B)

        sensors.append([x_S, y_S])
        beacons.append([x_B, y_B])
        distances.append(dist)

    return sensors, beacons, distances


def find_cannot(sensors, distances, y):

    cannot = []

    for sensor, dist in zip(sensors, distances):
        dy = abs(sensor[1] - y)
        if dy > dist:
            continue
        x_start = sensor[0] - (dist - dy)
        x_cannot = range(x_start, x_start + 2 * (dist - dy), 1)
        cannot += x_cannot

    return list(set(cannot))


def find_beacon(cannot):
    prune_range = set((range(4000000, 5200000, 1))).union(set((range(-1, -10000000, -1))))
    cannot_pruned = set(cannot) - prune_range
    print(len(cannot_pruned))
    if len(cannot_pruned) == 4000000:
        return None
    test_range = set(range(4000000))

    if len(test_range - cannot_pruned) > 0:
        res = test_range - cannot_pruned
        return int(list(res)[1])
    else:
        return None


def find_one_gap(senosrs, beacons, distances):
    eqs = []
    potential_y = []
    for i in range(len(senosrs)):
        for j in range(len(senosrs)):
            if i >= j:
                pass
            else:
                dist = distances[i] + distances[j]
                x_dist = abs(senosrs[i][0] - senosrs[j][0])
                y_dist = abs(senosrs[i][1] - senosrs[j][1])

                gap = (x_dist + y_dist) - dist
                print(gap)

                if gap in [0, 1, 2]:
                    try:
                        m = (sensors[j][1] - sensors[i][1]) / (sensors[j][0] - sensors[i][0])
                    except ZeroDivisionError:
                        m = 0
                    b = -m * senosrs[i][0] + senosrs[i][1]
                    eqs.append([m, b])

    for i in range(1,len(eqs), 1):
        x = (eqs[i][1] - eqs[i-1][1]) / (eqs[i-1][0] - eqs[i][0])
        y = eqs[i][0] * x + eqs[i][1]
        if x > 0 and x < 4000000 and y > 0 and y < 4000000:
            print([x, y])
            potential_y.append(int(y))

    return potential_y


def manhatten_distance(a_x, a_y, b_x, b_y):
    return abs(a_x - b_x) + abs(a_y - b_y)


def check_field_empty(y_index, x_index, sensors, beacons):
    for sensor in sensors:
        if manhatten_distance(x_index, y_index, sensor[0], sensor[1]) <= sensor[2]:
            return False
    for beacon in beacons:
        if y_index == beacon[1] and x_index == beacon[0]:
            return False
    return True


def traverse_border(sensor_x, sensor_y, distance, max_zone, sensors, beacons):
    if sensor_y - distance < 0:
        half_width = - (sensor_y - distance)
    else:
        half_width = 0
    # top
    top = sensor_y - distance - 1
    if top > 0:
        if check_field_empty(top, sensor_x, sensors, beacons):
            print('omg finally', 'y', top, 'x', sensor_x)
            print('solution', sensor_x * 4000000 + top)
            return True
    # bottom
    bottom = sensor_y + distance + 1
    if bottom <= max_zone + 1:
        if check_field_empty(bottom, sensor_x, sensors, beacons):
            print('omg finally', 'y', bottom, 'x', sensor_x)
            print('solution', sensor_x * 4000000 + bottom)
            return True
    # left and right
    for y in range(max(0, sensor_y - distance), min(sensor_y + distance + 1, max_zone + 1)):
        # left
        left = sensor_x - half_width - 1
        if left > 0:
            if check_field_empty(y, left, sensors, beacons):
                print('omg finally', 'y', y, 'x', left)
                print('solution', left * 4000000 + y)
                return True
        right = sensor_x + half_width + 1
        if right <= max_zone + 1:
            if check_field_empty(y, right, sensors, beacons):
                print('omg finally', 'y', y, 'x', right)
                print('solution', right * 4000000 + y)
                return True
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1
    return False


def save_no_beacon_zone(grid, sensor_x, sensor_y, distance, y_index):
    if sensor_y - distance < 0:
        half_width = - (sensor_y - distance)
    else:
        half_width = 0
    for y in range(sensor_y - distance, sensor_y + distance + 1):
        if y == y_index:
            for x in range(sensor_x - half_width, sensor_x + half_width + 1):
                grid.add(x)
        if y < sensor_y:
            half_width += 1
        else:
            half_width -= 1


def solve2(file, max_zone):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    sensors = []
    beacons = []
    for i, line in enumerate(lines):
        # print(line)
        parts_with_numbers = [word for word in line.split(' ') if '=' in word]
        parts_with_numbers_cleaned = [word.replace(',', '').replace(':', '') for word in parts_with_numbers]
        sensor_x, sensor_y, beacon_x, beacon_y = list(map(lambda x: int(x.split('=')[1]), parts_with_numbers_cleaned))

        distance_to_beacon = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        sensors.append([sensor_x, sensor_y, distance_to_beacon])
        beacons.append([beacon_x, beacon_y])

    for i, sensor in enumerate(sensors):
        print('sensor', i)
        if traverse_border(sensor[0], sensor[1], sensor[2], max_zone, sensors, beacons):
            return


# Part I

file = open("input_day15.txt", 'r')
lines = file.readlines()

sensors, beacons, distances = get_data(lines)
#cannot = find_cannot(sensors, distances, 2000000)
#print(len(cannot))

# Part II

potential_y = find_one_gap(sensors, beacons, distances)

#for y in potential_y:
#    cannot = find_cannot(sensors, distances, y)
#    found_x = find_beacon(cannot)
#    if found_x is not None:
#        found_y = y
#        print(found_x, found_y)
#        if found_x > 0 and found_y > 0:
#            pass
# print(found_x * 4000000 + found_y)

solve2("input_day15.txt", 4000000)
