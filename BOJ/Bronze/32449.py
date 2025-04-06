n = int(input())
others = []
max_pig = 0

for _ in range(n):
    s, i = input().split()
    i = int(i)
    if s == "pig":
        max_pig = max(max_pig, i)
    else:
        others.append(i)

res = max_pig
for i in others:
    if i < max_pig:
        res += i

print(res)