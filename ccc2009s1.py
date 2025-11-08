a,b = [int(input()) for _ in range(2)]

# SLOW: O(b-a) or O(n)

# eps = 1e-5

# def isint(x): # checks float x is integer
#     return abs(round(x) - x) < eps
# # with float, we don't check equality by x == round(x)
# #   because of precision issues

# res = 0
# from math import pow
# for i in range(a, b+1):
#     if isint(pow(i, 1/2)) and isint(pow(i, 1/3)):
#         res += 1
        
# print(res)

# FAST - O(b^(1/6)) or O(n^(1/6)) (almost O(1))

# these are the possibilities for the 6th root of the numbers
possibilities = range(int(a**(1/6)), int(b**(1/6)) + 2)

res = 0
for p in possibilities:
    if a <= p**6 <= b:
        res += 1

print(res)