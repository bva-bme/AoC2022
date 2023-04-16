from collections import deque


def bfs_shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def create_graph(lines):

    numerical_heights = []
    possible_starts = []
    for i, line in enumerate(lines):
        numerical_heights.append([])
        for j, char in enumerate(line[:-1]):
            numerical_heights[-1].append(ord(char) - 97)
            if char == 'S':
                start_idx = i * (len(line) - 1) + j
                numerical_heights[-1][-1] = 0
                possible_starts.append(i * (len(line) - 1) + j)
            if char == 'E':
                end_idx = i * (len(line) - 1) + j
                numerical_heights[-1][-1] = 122 - 97
            if char == 'a':
                possible_starts.append(i * (len(line) - 1) + j)


    graph = {}
    for i in range(len(numerical_heights)):
        for j in range(len(numerical_heights[i])):
            graph[i * len(numerical_heights[i]) + j] = []
            # check left
            if j > 0 and numerical_heights[i][j] >= numerical_heights[i][j-1] - 1:
                graph[i * len(numerical_heights[i]) + j].append(i * len(numerical_heights[i]) + j - 1)
            # check right
            if j < len(numerical_heights[i])-1 and numerical_heights[i][j] >= numerical_heights[i][j+1] - 1:
                graph[i * len(numerical_heights[i]) + j].append(i * len(numerical_heights[i]) + j + 1)
            # check up
            if i > 0 and numerical_heights[i][j] >= numerical_heights[i-1][j] - 1:
                graph[i * len(numerical_heights[i]) + j].append((i - 1) * len(numerical_heights[i]) + j)
            # check down
            if i < len(numerical_heights)-1 and numerical_heights[i][j] >= numerical_heights[i+1][j] - 1:
                graph[i * len(numerical_heights[i]) + j].append((i + 1) * len(numerical_heights[i]) + j)
    return graph, start_idx, end_idx, possible_starts

# Part I

file = open("input_day12.txt", 'r')
lines = file.readlines()

graph, start, end, possible_starts = create_graph(lines)
path = bfs_shortest_path(graph, start, end)
print(len(path) - 1)

file.close()

# Part II
minpath = 9999

for a in possible_starts:
    path = bfs_shortest_path(graph, a, end)
    if path and len(path) - 1 < minpath:
        minpath = len(path) - 1
print(minpath)