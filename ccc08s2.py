# # brute force (gets 9/15 test cases but TLEs on the rest)

# while True:
#     N = int(input())
#     if N == 0:
#         break
#     count = 0
#     for i in range(-N, N + 1):
#         for j in range(-N, N + 1):
#             if i**2 + j**2 <= N**2:
#                 count += 1  
#     print(count)

# math solution (gets 15/15 test cases)

import math

while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for x in range(-N, N + 1):
        largest_y = int(math.sqrt(N**2 - x**2))

        # for the points (x, -k) and (x, k) where k is from 1 to largest_y
        count += 2 * largest_y
        # for the point (x, 0)
        count += 1  
    print(count)