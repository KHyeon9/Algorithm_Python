x, y = map(int, input().split())
x = (100 - x) / 100
y = (100 - y) / 100
print((1 / x - 1) / (1 / y - 1))