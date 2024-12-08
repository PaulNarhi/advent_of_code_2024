import numpy as np
import itertools
import datetime

file = open('./input/input_day6.txt', 'r')
content = file.read()

lines = content.split('\n')
lines = np.array([list(l) for l in lines])

# a)

# x,y
dirs = itertools.cycle(((-1,0), (0, 1), (1, 0), (0, -1)))

x, y = np.where(lines == '^')
x, y = x[0], y[0]

visited = set()
loop_positions = set()
visited.add((x,y))
dx, dy = next(dirs)

while True:
    # new pos
    xn = x + dx
    yn = y + dy
    if not (0 <= xn < len(lines) and 0 <= yn < len(lines[0])):
        break
    if lines[xn][yn] == '#':
        dx, dy = next(dirs)
        continue
    x, y = xn, yn
    visited.add((x,y))

print(len(visited))

#b )


loop_positions = set()

for i in range(len(lines[0])):
    for j in range(len(lines)):
        orig = lines[i][j]
        if lines[i][j] != '^':
            lines[i][j] = '#'

        if i%10==0:
            print(f'ok{j}')
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
        current_dir = 0  

        x, y = np.where(lines == '^')
        x, y = x[0], y[0]

        visited = set()
        visited.add((x, y, current_dir)) 
        
        while True:

            dx, dy = dirs[current_dir]
            xn = x + dx
            yn = y + dy


            if not (0 <= xn < len(lines) and 0 <= yn < len(lines[0])):
                break

            if lines[xn][yn] == '#':
                current_dir = (current_dir + 1) % 4  
                continue

            if (xn, yn, current_dir) in visited:
                loop_positions.add((i, j))
                break

            x, y = xn, yn
            visited.add((x, y, current_dir))
        lines[i][j] = orig



# Output visited positions
print(len(loop_positions))
