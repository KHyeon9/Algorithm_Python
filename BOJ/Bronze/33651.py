s = input()
idx = 0
res = ""

for c in "UAPC":
    if c not in s:
        res += c
print(res)