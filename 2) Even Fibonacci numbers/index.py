def formula(until):
    a = 0
    b = 1
    sum = 0

    while a <= until:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b

    return sum


print("The answer is: ", formula(4000000))
