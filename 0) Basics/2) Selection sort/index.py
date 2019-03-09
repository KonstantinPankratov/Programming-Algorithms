def find_smallest(array):
    smallest_value = array[0]
    smallest_index = array.index(smallest_value)
    for i in range(len(array)):
        if array[i] < smallest_value:
            smallest_value = array[i]
            smallest_index = i
    return smallest_index


def sort(array):
    new_array = []
    for i in range(len(array)):
        item = find_smallest(array)
        item = array.pop(item)
        new_array.append(item)
    return new_array


array = [4, 7, 1, 2, 10]

print(sort(array))
