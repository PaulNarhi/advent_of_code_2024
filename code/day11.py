import regex as re
from functools import lru_cache

file = open('input/input_day11.txt')
digits = file.read()
# a)
nums = re.findall(r'(\d+)', digits)
nums = [int(num) for num in nums]

@lru_cache(maxsize=None)
def rules(num, count):
    if count == 0:
        return 1
    if num == 0:
        return rules(1, count - 1)
    if len(str(num)) % 2 == 0:
        half_len = len(str(num)) // 2
        first_half = int(str(num)[:half_len])
        second_half = int(str(num)[half_len:])
        return rules(first_half, count -1) + rules(second_half, count - 1)
    return rules(num * 2024, count - 1)
blinks = 25
print(sum([rules(n, blinks) for n in nums]))
# b)

blinks = 75
print(sum([rules(n, blinks) for n in nums]))