a, b = input().split()
a, b = a[::-1], b[::-1]
if len(b) > len(a):
    a, b = b, a
res = []

for i in range(len(a)):
    if i < len(b):
        res.append(str(int(a[i]) + int(b[i])))
    else:
        res.append(a[i])
print(*res[::-1], sep='')