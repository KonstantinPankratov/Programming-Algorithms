def formula(n):
    a = 2
    while a < n:
        if not n % a:
            n //= a  # a - factorial
        else:
            a += 1
    return n


print("The answer is: ", formula(600851475143))
