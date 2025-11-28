# Appleby Contest '19 P3 - A Recursion Problem

# Memoization
memory = {} # all the previous calculations

def calc(exp):
    '''
    
    calc takes in an infix notation and returns the value
    
    calc("(+ 1 1)") -> calc("1") + calc("1") -> 1 + 1 -> 2
    
    '''
    if exp in memory:
        return memory.get(exp)

    if "(" not in exp:
        res = int(exp)

        memory[exp] = res

        return res
    
    op = exp[1]
    first = ""
    second = ""

    ####### parsed the string and obtained the first and second

    res = 0
    if op == "+":
        res = calc(first) + calc(second)
    else:
        res = calc(first) - calc(second)

    memory[exp] = res
    
    return res

    