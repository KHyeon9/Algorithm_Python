n, m = map(int, input().split())
t = int(input())
x = [0, n]
y = [0, m]
result = 0

for i in range(t):
    cut, pos = map(int, input().split())
    if cut == 0:
        y.append(pos)
    else:
        x.append(pos)
x.sort()
y.sort()

for i in range(1, len(x)):
    for j in range(1, len(y)):
        w = x[i] - x[i - 1]
        h = y[j] - y[j - 1]
        result = max(result, w * h)
print(result)