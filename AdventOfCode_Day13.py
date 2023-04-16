def parse_element(line):
    return eval(line[:-1])


def compare(a, b, mixed=False):
    if isinstance(a, int) and isinstance(b, int):
        if a <= b:
            result = True
        else:
            result = False
    elif isinstance(a, int) and isinstance(b, list):
        tmp_a = [a]
        result = compare(tmp_a, b, mixed=True)
    elif isinstance(a, list) and isinstance(b, int):
        tmp_b = [b]
        result = compare(a, tmp_b, mixed=True)
    else:
        result = True
        for i, a_elem in enumerate(a):
            try:
                result = compare(a_elem, b[i])
                if result is False:
                    break
            except IndexError:
                if mixed:
                    break
                else:
                    result = False
                    break
    return result


# I had to cheat :(
def compare_lists(first, second):
    while len(first) > 0 and len(second) > 0:
        left = first.pop(0)
        right = second.pop(0)
        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            sub_comparison = compare_lists(left, right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == int and type(right) == list:
            sub_comparison = compare_lists(list([left]), right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == list and type(right) == int:
            sub_comparison = compare_lists(left, list([right]))
            if sub_comparison != 0:
                return sub_comparison
    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1
    else:
         return 0


# modified bubble sort
def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if compare_lists(parse_element(elements[i]), parse_element(elements[i + 1])) != 1:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return

# Part I

file = open("input_day13.txt", 'r')
lines = file.readlines()

n = int(len(lines) / 3) + 1

idx_sum = 0

for i in range(n):
    list_a = parse_element(lines[i*3])
    list_b = parse_element(lines[i*3 + 1])

    result = compare_lists(list_a, list_b)
    if result == 1:
        idx_sum += i+1
print(idx_sum)

# Part II
lines_2 = []
for line in lines:
    if line == '\n':
        pass
    else:
        lines_2.append(line)
lines_2.append('[[2]]\n')
lines_2.append('[[6]]\n')

bubblesort(lines_2)

idx_2 = 0
idx_6 = 0

for i, line in enumerate(lines_2):
    if line == '[[2]]\n':
        idx_2 = i+1
    elif line == '[[6]]\n':
        idx_6 = i+1
key = idx_2 * idx_6
print(key)