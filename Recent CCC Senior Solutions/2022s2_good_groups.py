import sys

input = sys.stdin.readline

d = {}
x = int(input())
for _ in range(x):
    a,b = input().split()
    d[(a,b)]=True

y = int(input())
for _ in range(y):
    a,b = input().split()
    d[(a,b)] = False

groups = {}
g = int(input())
for i in range(g):
    a,b,c = input().split()

    groups[a], groups[b], groups[c] = i, i, i

res = 0
for a,b in d:
    cond = d[(a,b)]
    if cond and groups[a] != groups[b]:
        res += 1
    elif not cond and groups[a] == groups[b]:
        res += 1

print(res)