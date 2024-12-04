import numpy as np
import re

# a)

file = open('input_day3.txt', 'r')
content = file.read()
commands = re.findall(f"mul\(\d+,\d+\)", content)
print(commands)
#print(sum([int(i.split(",")[0][4:]) * int(i.split(",")[1][:-1]) for i in commands]))

# b)
file = open('input_day3.txt', 'r')
content = file.read()
commands = re.findall(f"mul\(\d+,\d+\)|do\(\)|don't\(\)", content)

do_active = True
ans = 0
for command in commands:
    if command == 'don\'t()':
        do_active = False
        continue
    if command[0:3] == 'mul' and do_active:
        ans += int(command.split(",")[0][4:]) * int(command.split(",")[1][:-1])
        continue
    if command == 'do()':
        do_active = True
        continue

print(ans)
