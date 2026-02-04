# Greedy algorithms: sorting is usually required

# number of intervals
n = int(input())

L = []

for _ in range(n):
    a, b = map(int, input().split())
    L.append((a,b)) # using tuples to save time because of immutability of tuples

L.sort(key=lambda x: x[1]) # sort by finishing time

went = 0
next_available_time = 0
for a, b in L:
    if next_available_time >= b:
        continue

    go_at = max(a, next_available_time)
    went += 1
    next_available_time = go_at + 1

print(went)
