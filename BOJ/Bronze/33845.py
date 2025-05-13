s = input()
t = input()
res = ""

for ch in t:
    if ch not in s:
        res += ch

print(res)