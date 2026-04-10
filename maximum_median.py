# Maximum Median CodeForces - 1201C

n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# leftmost index of the second half of the array
mid = len(a) // 2

def check(x):
    need = 0

    for i in range(mid, len(a)):
        if a[i] < x:
            need += x - a[i]

        if need > k:
            return False
    
    return True

left, right = min(a), max(a) + k

while left < right:
    guess = (left + right + 1) // 2
    # print(guess, check(guess))

    if check(guess):
        left = guess
    else:
        right = guess - 1

print(left)