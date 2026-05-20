n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = a[n // 2]
i = n // 2 + 1

while i < n and k > 0:
    diff = a[i] - ans
    if diff * (i - n // 2) <= k:
        ans += diff
        k -= diff * (i - n // 2)
    else:
        ans += k // (i - n // 2)
        k = 0
    i += 1

if k > 0:
    ans += k // (n - n // 2)

print(ans)