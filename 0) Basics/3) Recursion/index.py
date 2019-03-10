def countdown(a):
    print(a)
    while a > 1:
        countdown(a - 1)
        break


def countdown2(a):
    if a > 1:
        print(a)
        countdown(a - 1)
    else:
        return


countdown(10)
countdown2(10)
