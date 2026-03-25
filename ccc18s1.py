N = int(input())

L = [int(input()) for _ in range(N)]

L.sort()

bound = float('-inf')
prev = None
res = float('inf')
for n in L:
    if prev != None:
        new_bound = (n - prev) / 2 + prev

        res = min(res, new_bound - bound)

        bound = new_bound
    
    prev = n
print(res)