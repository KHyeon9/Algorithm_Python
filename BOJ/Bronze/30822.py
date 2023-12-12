n = int(input())
s = input()
res = []

for w in "uospc":
    res.append(s.count(w))

print(min(res))


