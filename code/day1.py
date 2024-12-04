import numpy as np
from cryptography.fernet import Fernet



# a)
file = open('./input/input_day1.txt', 'r')
content = file.read()
rows = content.split("\n")
first_col = [int(r.split("   ")[0]) for r in rows]
second_col = [int(r.split("   ")[1]) for r in rows]
print(np.sum(np.abs(np.subtract(np.sort(first_col), np.sort(second_col)))))

# b)
file = open('./input/input_day1.txt', 'r')
content = file.read()
rows = content.split("\n")
first_col = [int(r.split("   ")[0]) for r in rows]
second_col = np.array([int(r.split("   ")[1]) for r in rows])

sim_score = 0
for n in first_col:
    count = sum(second_col == n)
    sim_score += count * n
print(sim_score)