# Part I
import numpy as np


file = open("input_day8.txt", 'r')
lines = file.readlines()

matrix = []
for line in lines:
    matrix.append([*line[:-1]])
np_trees = np.array(matrix, dtype=int)

num_visible = 0
for i in range(np_trees.shape[1]):
    for j in range(np_trees.shape[0]):
        current_height = np_trees[i][j]
        top_slice = np_trees[:j+1,i]
        bottom_slice = np_trees[j:,i]
        right_slice = np_trees[j,i:]
        left_slice = np_trees[j,:i+1]
        bottom_slice = np.flip(bottom_slice)
        right_slice = np.flip(right_slice)

        if top_slice.size == 1 or bottom_slice.size == 1 or right_slice.size == 1 or left_slice.size == 1:
            num_visible += 1
        else:
            for tree in top_slice[:-1]:
                if tree >= top_slice[-1]:
                    visible_top = False
                    break
                else:
                    visible_top = True
            for tree in bottom_slice[:-1]:
                if tree >= bottom_slice[-1]:
                    visible_bottom = False
                    break
                else:
                    visible_bottom = True
            for tree in right_slice[:-1]:
                if tree >= right_slice[-1]:
                    visible_right = False
                    break
                else:
                    visible_right = True
            for tree in left_slice[:-1]:
                if tree >= left_slice[-1]:
                    visible_left = False
                    break
                else:
                    visible_left = True
            if visible_left or visible_right or visible_bottom or visible_top:
                num_visible += 1

print(num_visible)

file.close()

# Part II

max_scenic_score = 0
for i in range(np_trees.shape[1]):
    for j in range(np_trees.shape[0]):
        if j == 2 and i == 3:
            print("ad")
        current_height = np_trees[i][j]
        top_slice = np_trees[:i+1,j]
        bottom_slice = np_trees[i:,j]
        right_slice = np_trees[i,j:]
        left_slice = np_trees[i,:j+1]
        top_slice = np.flip(top_slice)
        left_slice = np.flip(left_slice)

        visible_top = 0
        visible_bottom = 0
        visible_right = 0
        visible_left = 0

        for tree in top_slice[1:]:
            if tree < top_slice[0]:
                visible_top += 1
            else:
                visible_top += 1
                break
        for tree in bottom_slice[1:]:
            if tree < bottom_slice[0]:
                visible_bottom += 1
            else:
                visible_bottom += 1
                break
        for tree in left_slice[1:]:
            if tree < left_slice[0]:
                visible_left += 1
            else:
                visible_left += 1
                break
        for tree in right_slice[1:]:
            if tree < right_slice[0]:
                visible_right += 1
            else:
                visible_right += 1
                break

        scenic_score = visible_left * visible_right * visible_top * visible_bottom
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
