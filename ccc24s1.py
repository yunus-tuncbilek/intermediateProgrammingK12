N = int(input())

L = [int(input()) for _ in range(N)]

res = 0

half_length = N // 2

for i in range(half_length):
    if L[i] == L[i + half_length]:
        res += 2

print(res)