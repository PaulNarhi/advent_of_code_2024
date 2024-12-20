from collections import deque
from copy import copy
import time



file_path = 'input/input_day20.txt'
grid = {}
with open(file_path, 'r') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == 'S':
                start = (x, y)
            if char == 'E':
                end = (x, y)
            grid[(x, y)] = char

current = start
visited = set()
visited.add(current)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

scores = {start : 0}


while grid[current] != 'E':
    for d in dirs:
        next_pos = (current[0] + d[0], current[1] + d[1])
        if grid[next_pos] in ['.', 'E', 'S'] and next_pos not in visited:
            visited.add(next_pos)
            scores[next_pos] = scores[current] + 1
            current = next_pos
            break

start_time = time.time()
cheat = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), (0, 0), 
 (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)]

ans = 0

for location, score in scores.items():
    for d in cheat:
        next_pos = (location[0] + d[0], location[1] + d[1])
        nscore = scores.get(next_pos)
        if nscore:
            if nscore - score - abs(d[0]) - abs(d[1]) >= 100:
                ans += 1

print(ans)
print("Execution time for a):", time.time() - start_time, "seconds")

# b)
start_time = time.time()

def generateManhattanPoints(x, y, r):
    points = []
    for offset in range(r):
        invOffset = r - offset  # Inverse offset
        points.append((x + offset, y + invOffset))
        points.append((x + invOffset, y - offset))
        points.append((x - offset, y - invOffset))
        points.append((x - invOffset, y + offset))
    return points

cheat = [generateManhattanPoints(0, 0, d) for d in range(1, 21)]
cheat = [point for sublist in cheat for point in sublist]

ans = 0

for location, score in scores.items():
    for d in cheat:
        next_pos = (location[0] + d[0], location[1] + d[1])
        nscore = scores.get(next_pos)
        if nscore:
            if nscore - score - abs(d[0]) - abs(d[1]) >= 100:
                ans += 1

print(ans)
print("Execution time for b):", time.time() - start_time, "seconds")