def sort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        # main is a first element in array
        main = array[0]
        # less is an array with elements which less than main
        less = []
        # greater is an array with elements which greater than main
        greater = []

        for i in array[1:]:
            if i < main:
                less.append(i)
            elif i > main:
                greater.append(i)

        return sort(less) + [main] + sort(greater)


print(sort([23, 1, 17, 51]))
