import heapq
import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())

P = [0] * (N + 1)
C = [0] * (N + 1)

# Heaps for each color: color_heaps[color] = [(-prettiness, pen_id)]
color_heaps = [[] for _ in range(M + 1)]

for i in range(1, N + 1):
    C[i], P[i] = map(int, input().split())
    heapq.heappush(color_heaps[C[i]], (-P[i], i))

# Global tracking
best_per_color = [0] * (M + 1)
total_best_sum = 0

# Heaps for the swap logic
# global_bests: min-heap of prettiness of eacb color's best pen
# global_spares: max-heap of prettiness of all pens NOT currently the best (stored as negative prettiness for max-heap)
global_bests = []
global_spares = []

def refresh_color(c):
    global total_best_sum
    # Remove old best from sum
    total_best_sum -= best_per_color[c]
    
    # Clean up the color heap (Lazy Deletion)
    while color_heaps[c]:
        neg_p, idx = color_heaps[c][0]
        if C[idx] == c and P[idx] == -neg_p:
            break
        heapq.heappop(color_heaps[c])
    
    if not color_heaps[c]:
        best_per_color[c] = 0
    else:
        # New best for this color
        top_p = -color_heaps[c][0][0]
        best_per_color[c] = top_p
        total_best_sum += top_p
        
        # Push to global bests (to find the smallest "best")
        heapq.heappush(global_bests, (top_p, c))
        
        # Any pen that isn't the top should be pushed to spares
        # Note: This approach handles spares lazily during the query phase

for c in range(1, M + 1):
    refresh_color(c)

# For spares, we initially push everything. 
# The query phase will filter out which ones are actually "top" pens.
for i in range(1, N + 1):
    heapq.heappush(global_spares, (-P[i], i))

def get_answer():
    # 1. Clean global_bests to find the true minimum 'best' pen
    while global_bests:
        p, c = global_bests[0]
        if best_per_color[c] == p:
            break
        heapq.heappop(global_bests)
    
    # 2. Clean global_spares to find the true maximum 'spare' pen
    # A pen is a valid spare if its (P, C) is current AND it's NOT the top of its color heap
    while global_spares:
        neg_p, idx = global_spares[0]
        p = -neg_p
        if P[idx] == p and C[idx] != 0:
            c = C[idx]
            # Check if it's the current best of its color
            if not (color_heaps[c] and color_heaps[c][0][1] == idx):
                break
        heapq.heappop(global_spares)
        
    ans = total_best_sum
    if global_bests and global_spares:
        potential_gain = (-global_spares[0][0]) - global_bests[0][0]
        if potential_gain > 0:
            ans += potential_gain
    return ans

print(get_answer())

for _ in range(Q):
    type, i, val = map(int, input().split())
    if type == 1:
        new_c = val
        old_c = C[i]
        C[i] = new_c
        heapq.heappush(color_heaps[new_c], (-P[i], i))
        heapq.heappush(global_spares, (-P[i], i))
        refresh_color(old_c)
        refresh_color(new_c)
    else:
        new_p = val
        P[i] = new_p
        c = C[i]
        heapq.heappush(color_heaps[c], (-new_p, i))
        heapq.heappush(global_spares, (-new_p, i))
        refresh_color(c)
    
    print(get_answer())