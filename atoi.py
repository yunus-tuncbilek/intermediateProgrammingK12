# recursive approach

def atoi(s):
    if s and s[0] == '-': # accommodates negative numbers
        return (-1) * atoi(s[1:])

    if s == "": # base case
        return 0
    
    # recursive case
    res = int(s[-1])

    recursive_step = atoi(s[:-1]) * 10
    res += recursive_step 

    return res

# iterative approach

def atoi_iter(s):
    negative = False
    if s and s[0] == "-":
        negative = True
        s = s[1:] # truncate the first elem
    
    res = 0
    # we are sure s is just made up of numbers
    for digit in s:
        res = int(digit) + res * 10

    # ternary operators: in Python they look like IF_VAL if COND else ELSE_VAL
    return (res if not negative else -res)

print(atoi_iter("12131"))