# Appleby Contest '19 P3 - NOT A Recursion Problem

def calc(exp):
    '''
    
    calc takes in an infix notation and returns the value
    
    calc("(+ 1 1)") -> calc("1") + calc("1") -> 1 + 1 -> 2
    
    '''
    res = 0
    curr = 0
    sign = 1
    for n in exp:
        if n.isnumeric():
            curr = curr * 10 + int(n)
        elif n == "-":
            sign = -1
        else:
            res += sign * curr
            curr = 0
            sign = 1
    res += sign * curr
    return res


# print(calc("(+ 1 2)"))
# print(calc("(+ 1 (+ (+ (+ 3 4) -2) 5))"))
print(calc(input()))