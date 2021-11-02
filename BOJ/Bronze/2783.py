x, y = map(int, input().split())
n = int(input())
r = x * (1000 / y)

for i in range(n):
    xi, yi = map(int, input().split())
    v = xi * (1000 / yi)

    if r > v:
        r = v


print("%.2f" % r)