import regex as re
from functools import cmp_to_key

file = open('./input/input_day5.txt', 'r')
content = file.read()
# a)
rules = content.split("\n\n")[0]
pages = content.split("\n\n")[1]

rules = re.findall(r"\d+\|\d+", rules)
rules = [list(map(int, r.split("|"))) for r in rules]
rules_d = {}
for k, v in rules:
    rules_d.setdefault(k, set()).add(v)
#print(rules_d)

pages = pages.split("\n")
pages = [list(map(int, p.split(","))) for p in pages]

result = 0
for p in pages:
    seen_pages = set()
    for e in p:
        if e in rules_d:
            if bool(rules_d[e] & seen_pages):
                # not legit
                break
        seen_pages.add(e)
    else:
        result += p[len(p) // 2]                

print(result)

# b)

def compare(l, r):
    if r in rules_d and l in rules_d[r]:
        return 1
    elif l in rules_d and r in rules_d[l]:
        return -1
    return 0
answer = 0
for p in pages:
    correct = sorted(p, key=cmp_to_key(compare)) 
    if p != correct:
        answer += correct[len(correct) // 2]

print(answer)