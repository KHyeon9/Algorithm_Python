s = input()
res = ""

if 'A' in s:
    for i in s:
        if i in ['B', 'C', 'D', 'F']:
            res += 'A'
        else:
            res += i
elif 'B' in s:
    for i in s:
        if i in ['C', 'D', 'F']:
            res += 'B'
        else:
            res += i
elif 'C' in s:
    for i in s:
        if i in ['D', 'F']:
            res += 'C'
        else:
            res += i
else:
    res = len(s) * 'A'
print(res)