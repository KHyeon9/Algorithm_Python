li = list(input().split())
res = li[0]

for el in li[1:]:
    if res[-1] == el[0]:
        res += "'" + el[1:]
        continue
    res += el
print(res)