import regex as re
from itertools import product

file = open('./input/input_day7.txt', 'r')
content = file.read()
rows = content.split("\n")

# a)
if False:
    operations = "*+"
    answer = 0
    for row in rows:
        nums = [int(i) for i in re.findall(r"\d+", row)]
        ans = nums[0]
        operations_count = len(nums) - 2
        for perm in product(operations, repeat=operations_count):
            result = nums[1]
            for idx, op in enumerate(perm):
                result = result + nums[idx+2] if op == '+' else result * nums[idx+2]
            if result == nums[0]:
                answer += nums[0]
                break
    print(answer)

# b)
operations = "*+|"
answer = 0
for row in rows:
    nums = [int(i) for i in re.findall(r"\d+", row)]
    ans = nums[0]
    operations_count = len(nums) - 2
    for perm in product(operations, repeat=operations_count):
        result = nums[1]
        for idx, op in enumerate(perm):
            if op == '+':
                result = result + nums[idx+2] 
            elif op == '*': 
                result = result * nums[idx+2] 
            else:
                result = int(str(result) + str(nums[idx+2]))
        if result == nums[0]:
            answer += nums[0]
            break
print(answer)