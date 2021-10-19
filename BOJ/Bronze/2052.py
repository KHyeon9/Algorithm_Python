n = int(input())
a = "%.300f" % (1 / (2 ** n))
l = len(a)
for i in range(l - 1, 1, -1):
    if a[i] != '0':
        last = i
        break
print(a[:last + 1])
