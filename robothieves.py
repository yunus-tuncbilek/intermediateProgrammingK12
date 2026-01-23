# Solve Robothieves problem from CCC 
# https://dmoj.ca/problem/ccc15s3

from collections import deque
import sys # For BFS queue

R, C = input().split()
R = int(R)
C = int(C)

grid = []
for _ in range(R):
    row = input().strip()
    grid.append(row)

# 1. Pre-process Cameras
# is_blocked tracks walls AND camera lines of sight
is_blocked = [[False for _ in range(C)] for _ in range(R)]
start_pos = None
empty_cells = [] 
# How to keep track of both the row number and cells? 
# Make a list per cell ([3,5]) or a tuple ( (3,5) faster)

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'W':
            is_blocked[r][c] = True
        elif grid[r][c] == 'S':
            start_pos = (r, c)
        elif grid[r][c] == '.':
            empty_cells.append((r, c))
        elif grid[r][c] == 'C':
            is_blocked[r][c] = True
            # Mark camera vision in 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curr_r, curr_c = r + dr, c + dc
                while 0 <= curr_r < R and 0 <= curr_c < C:
                    if grid[curr_r][curr_c] == 'W':
                        break
                    # Cameras can see through everything EXCEPT walls
                    if grid[curr_r][curr_c] in ('.', 'S', 'L', 'R', 'U', 'D'):
                        is_blocked[curr_r][curr_c] = True
                    curr_r += dr
                    curr_c += dc

# 2. BFS Setup
# If the start is in a camera zone, we can't move at all
if is_blocked[start_pos[0]][start_pos[1]]:
    for _ in empty_cells:
        print("-1")
    sys.exit()

distances = [[-1 for _ in range(C)] for _ in range(R)]
queue = deque([start_pos])
distances[start_pos[0]][start_pos[1]] = 0

# 3. BFS Execution
while queue:
    r, c = queue.popleft()

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc

        # Process movement logic (especially conveyors)
        while True:
            if grid[nr][nc] == 'W' or is_blocked[nr][nc]:
                break # Hit a wall or camera zone
            
            if grid[nr][nc] == '.':
                if distances[nr][nc] == -1:
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))
                break
            
            # Conveyor logic: Slide until we hit a non-conveyor cell
            if grid[nr][nc] == 'L': nc -= 1
            elif grid[nr][nc] == 'R': nc += 1
            elif grid[nr][nc] == 'U': nr -= 1
            elif grid[nr][nc] == 'D': nr += 1
            else:
                # Landing on 'S' (treated as empty space)
                if distances[nr][nc] == -1:
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))
                break

# 4. Final Output
for r, c in empty_cells:
    print(distances[r][c])