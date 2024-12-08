import numpy as np
from collections import defaultdict
from itertools import combinations

file = open('./input/input_day8.txt', 'r')
content = np.array([list(i) for i in file.read().split('\n')])
antennas = content[content != '.']
antenna_coords = np.argwhere(content != '.')
combined = zip(antennas, antenna_coords)

antenna_dict = defaultdict(list)
for antenna, coord in combined:
    antenna_dict[antenna].append(tuple(coord))

all_points = set()
for antenna_coords in antenna_dict.values():
    pairs = combinations(antenna_coords, 2)
    for pair in pairs:
        x1, y1 = pair[0]; x2, y2 = pair[1]
        point1 = 2 * np.array([x1 - x2, y1 - y2]) + np.array([x2, y2])
        point2 = -1 * np.array([x1 - x2, y1 - y2]) + np.array([x2, y2])
        all_points.add(tuple(point1))
        all_points.add(tuple(point2))

# filter out of bounds
rows, cols = content.shape  # Dimensions of the grid

# Filter points that are within bounds
filtered_points = {
    tuple(point) for point in all_points
    if 0 <= point[0] < rows and 0 <= point[1] < cols
}

print(len(filtered_points))

# b)

file = open('./input/input_day8.txt', 'r')
content = np.array([list(i) for i in file.read().split('\n')])
antennas = content[content != '.']
antenna_coords = np.argwhere(content != '.')
combined = zip(antennas, antenna_coords)

antenna_dict = defaultdict(list)
for antenna, coord in combined:
    antenna_dict[antenna].append(tuple(coord))

all_points = set()
for antenna_coords in antenna_dict.values():
    pairs = combinations(antenna_coords, 2)
    for pair in pairs:
        x1, y1 = pair[0]; x2, y2 = pair[1]
        for k in range(-50, 50):
            point = k * np.array([x1 - x2, y1 - y2]) + np.array([x2, y2])
            all_points.add(tuple(point))

# filter out of bounds
rows, cols = content.shape  # Dimensions of the grid

# Filter points that are within bounds
filtered_points = {
    tuple(point) for point in all_points
    if 0 <= point[0] < rows and 0 <= point[1] < cols
}

print(len(filtered_points))