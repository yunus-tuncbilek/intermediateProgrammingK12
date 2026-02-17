import sys

# Read input: N = number of points, C = circumference
line1 = sys.stdin.readline().split()
if not line1:
    exit()
n, c = map(int, line1)

line2 = sys.stdin.readline().split()
if not line2:
    points = []
else:
    points = list(map(int, line2))

good_triplets = 0
limit = c / 2

# Triple nested loop to check every combination
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # Pick the three points
            p = sorted([points[i], points[j], points[k]])
            
            # Calculate the three distances between them along the circle
            # d1: dist between point 1 and 2
            # d2: dist between point 2 and 3
            # d3: dist between point 3 and 1 (wrapping around the circle)
            d1 = p[1] - p[0]
            d2 = p[2] - p[1]
            d3 = c - (p[2] - p[0])
            
            # A triplet is "Good" if it contains the center.
            # This only happens if NO distance between points is >= C/2.
            if d1 < limit and d2 < limit and d3 < limit:
                good_triplets += 1

print(good_triplets)