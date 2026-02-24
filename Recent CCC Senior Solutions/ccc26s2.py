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

# we will take the prefix sum to get the number of lights at each parking space
for i in range(1, N + 1):
    arr[i] += arr[i - 1]

print(arr)

reqs = []
mem = {}
for _ in range(R):
    reqs.append(int(input()))
    mem[reqs[-1]] = False

# we will check if the parking space is lit or not
for i in range(N + 1):
    if arr[i] > 0 and i in mem:
        mem[i] = True

# we will print the result for each request
for req in reqs:
    if mem[req]:
        print("Light")
    else:
        print("Dark")
