

file = open('./input/input_day10.txt', 'r')
lines = file.readlines()
file.close()
grid = [list(map(int, list(line.strip()))) for line in lines]

def get_element(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return None
    return grid[i][j]

trailheads = []
for i, _ in enumerate(grid):
    for j, _ in enumerate(grid[0]):
        if grid[i][j] == 0:
            trailheads.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

trailhead_scores_a = []
trailhead_scores_b = []
stack = []
for trailhead in trailheads:
    stack.append(trailhead)
    score_a = set()
    score_b = 0
    while stack:
        current = stack.pop()
        i, j = current
        current_element = get_element(grid, i, j)
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]
            element = get_element(grid, new_i, new_j)
            if element is not None and element == current_element + 1:
                if current_element == 8 and element == 9:
                    score_a.add((new_i, new_j))
                    score_b += 1
                    continue
                stack.append((new_i, new_j))
    trailhead_scores_a.append(len(score_a))
    trailhead_scores_b.append(score_b)
print(f"Part 1: {sum(trailhead_scores_a) }; Part 2: {sum(trailhead_scores_b)}")