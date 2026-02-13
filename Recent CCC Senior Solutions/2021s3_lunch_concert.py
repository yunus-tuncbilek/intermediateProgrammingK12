import sys

input = sys.stdin.readline

N = int(input())
concerts = [[int(a) for a in input().split()] for _ in range(N)]

leftmost = float('inf')
rightmost = float('-inf')
for p, w, d in concerts:
    leftmost = min(p, leftmost)
    rightmost = max(p, rightmost)

def time(c):
    res = 0
    for p, w, d in concerts:
        if p < c:
            res += w * (max(0, c - d - p))
        else:
            res += w * (max(0, p - (c + d)))
                        
    return res

left, right = leftmost, rightmost
while left < right:
    mid = (left+right) // 2

    if mid == leftmost or mid == rightmost:
        break

    if time(mid - 1) < time(mid) and time(mid) < time(mid + 1):
        right = mid - 1
    elif time(mid - 1) > time(mid) and time(mid) > time(mid + 1):
        left = mid + 1
    else:
        left, right = mid, mid

print(time(left))

    