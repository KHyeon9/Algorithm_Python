s = input()
res = 1

for w in set(list(s)):
    if s.count(w) > 1:
        res = 0
        break

print(res)
