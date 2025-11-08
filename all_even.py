n = int(input())

res = n

def even_digits(n):
    # all keyword/function in python
    # all(a list or a generator) is true if the expression 
    # is true for all elements of the list / generator
    return all(int(d) % 2 == 0 for d in str(n))

while not even_digits(res):
    res += 1

print(res)