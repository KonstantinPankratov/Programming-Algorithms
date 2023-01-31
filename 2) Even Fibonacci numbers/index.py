def formula(until):
    a = 0
    b = 1
    sum = 0

    while a <= until:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b

    return sum

def formula_2(until):
    if (until < 2):
        return 0
    
    a = 0
    b = 2
    sum= a + b
    
    while (b <= until):
        c = 4 * b + a
        
        if (c > until):
            break
            
        a = b
        b = c
        sum = sum + b
        
    return sum

print("The answer is: ", formula(4000000))
