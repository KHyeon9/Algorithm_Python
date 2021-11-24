t = int(input())
r = 0
a = []
b = []

for i in range(t - 1):
    s, d, c = list(map(int, input().split()))
    a.append(d)
    b.append(c)

for i in range(t - 1):
    r ^= b[i]
print(r)