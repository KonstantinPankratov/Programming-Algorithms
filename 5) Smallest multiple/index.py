def func():
    for i in range(1000, 1000000000, 20):  # Step 20, because the desired number is a multiple of 20
        for x in range(11, 21):  # No need to check all dividers (16 % 4 => 16 % 2)
            if i % x != 0:  # Break the loop if there's a remainder
                break
            if x == 20:  # if i passes all checks => desired number
                return i
    return None


print("The answer is: ", func())
