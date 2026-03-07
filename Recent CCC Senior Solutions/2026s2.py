# number of parking spaces
N = int(input())

arr = [0] * (N + 1)

# number of lights
M = int(input())

# number of requests
R = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    leftmost = max(0, a - b)
    right_end = a + b + 1

    # we will add 1 to the leftmost and subtract 1 from the rightmost 
    # to indicate the range of lights
    arr[leftmost] += 1
    if right_end <= N: 
        arr[right_end] -= 1 

# prefix_sums = [0] * (N + 1)
# we will take the prefix sum to get the number of lights at each parking space
for i in range(1, N + 1):
    arr[i] += arr[i - 1]

reqs = []
for _ in range(R):
    count = arr[int(input())]
    if count > 0:
        print("Light")
    else:
        print("Dark")