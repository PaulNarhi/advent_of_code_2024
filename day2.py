import numpy as np

# a)
file = open('input_day2.txt', 'r')
content = file.read()
rows = content.split("\n")
rows = [row.split(" ") for row in rows]

count = 0
for row in rows:
    int_row = [int(e) for e in row]
    diffs = np.diff(int_row)
    if val := all(item > 0 for item in diffs) or all(item < 0 for item in diffs):
        if all(abs(diffs) < 4 ):
            count += 1
#print(count)

# b)

def is_safe(row):
    int_row = [int(e) for e in row]
    diffs = np.diff(int_row)
    if all(item > 0 for item in diffs) or all(item < 0 for item in diffs):
        if all(abs(diffs) < 4 ):
            return True
    return False


count = 0
for row in rows:
    if is_safe(row):
        count += 1
        continue
    else:
        for i in range(len(row)):
            if is_safe(row[0:i] + row[i+1:]):
                count += 1
                break
print(count)