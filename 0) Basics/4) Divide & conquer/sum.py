def sum(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + sum(array[1:])


print(sum([2, 4, 6]))
