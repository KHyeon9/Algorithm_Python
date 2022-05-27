n = int(input())
x_li = []
y_li = []
for i in range(n):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)
x_li.sort()
y_li.sort()
print((x_li[-1] - x_li[0]) * (y_li[-1] - y_li[0]))