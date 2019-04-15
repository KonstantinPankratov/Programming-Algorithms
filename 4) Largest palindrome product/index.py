def find_largest_palindrome(multiplicand, multiplier):
    palindromes = []

    for i in range(multiplier, multiplicand - 1, -1):
        for j in range(i, multiplicand - 1, -1):
            if is_palindrome(i*j):
                palindromes.append(i*j)

    largest_palindrome = max(palindromes)

    return largest_palindrome


def find_largest_palindrome_2(multiplicand, multiplier):
    palindrome = 1

    for i in range(multiplier, multiplicand - 1, -1):
        for j in range(i, multiplicand - 1, -1):
            if is_palindrome(i*j):
                if i*j > palindrome:
                    palindrome = i*j

    return palindrome


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


print("The answer is: ", find_largest_palindrome(100, 999))
