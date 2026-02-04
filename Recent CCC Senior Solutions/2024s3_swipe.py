import sys

input = sys.stdin.readline
# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1. Group target array B into segments (value, start_index, end_index)
segments = []
if n > 0:
    curr_val = b[0]
    start_idx = 0
    for i in range(1, n):
        if b[i] != curr_val:
            segments.append((curr_val, start_idx, i - 1))
            curr_val = b[i]
            start_idx = i
    segments.append((curr_val, start_idx, n - 1))

# 2. Greedy Two-Pointer: Find each segment's "source" index in A
source_indices = []
a_ptr = 0
for val, start, end in segments:
    while a_ptr < n and a[a_ptr] != val:
        a_ptr += 1
    
    if a_ptr == n:
        print("NO")
        sys.exit(0)
    
    source_indices.append(a_ptr)
    a_ptr += 1 # Move past this used element

# 3. Generate Swipes
# We must be careful: Left swipes move left, Right swipes move right.
# To avoid overwriting our 'source' elements, we process:
# - Left swipes from index 0 to M (Left to Right)
# - Right swipes from index M to 0 (Right to Left)

l_moves = []
r_moves = []

for i in range(len(segments)):
    val, target_start, target_end = segments[i]
    src = source_indices[i]
    
    if src > target_start:
        l_moves.append(f"L {target_start} {src}")
    if src < target_end:
        r_moves.append(f"R {src} {target_end}")

# Output results
print("YES")
# Combine L moves (ordered L to R) and R moves (ordered R to L)
total_moves = l_moves + r_moves[::-1]
print(len(total_moves))
for move in total_moves:
    print(move)