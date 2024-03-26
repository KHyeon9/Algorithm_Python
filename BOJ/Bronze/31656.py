s = input()
res, temp = "", ""

for w in s:
    if temp != w:
        temp = w
        res += w

print(res)

