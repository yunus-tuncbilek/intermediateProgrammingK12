# Appleby Contest '19 P3 - A Recursion Problem

# Memoization
memory = {} # all the previous calculations

def calc(exp):
    '''
    
    calc takes in an infix notation and returns the value
    
    calc("(+ 1 1)") -> calc("1") + calc("1") -> 1 + 1 -> 2
    
    '''
    # print(exp)

    if exp in memory:
        return memory.get(exp)

    if "(" not in exp: # exp must be just a number
        res = int(exp)

        memory[exp] = res

        return res
    
    # exp = (+/- exp1 exp2)
    op = exp[1] # + or -
    first = ""
    second = ""

    ####### parse the exp string and obtained the first and second exps
    right_space = None
    p, depth = 3, 0
    while p < len(exp):
        if exp[p] == "(":
            depth += 1
        elif exp[p] == ")":
            depth -= 1

        if exp[p] == " " and depth == 0:
            right_space = p
            break

        p += 1

    first = exp[3:right_space] # first expression
    second = exp[right_space + 1:len(exp) - 1] # second expression

    res = 0
    if op == "+":
        res = calc(first) + calc(second)
    else:
        res = calc(first) - calc(second)

    memory[exp] = res
    
    return res

# print(calc("(+ 1 2)"))
# print(calc("(+ 1 (+ (+ (+ 3 4) -2) 5))"))
print(calc(input()))