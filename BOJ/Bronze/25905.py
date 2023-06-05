ratio = sorted([float(input()) for _ in range(10)], reverse=True)
res = 1

for i in range(1, 10):
    res *= ratio[i - 1] / i
print(round(res * (10 ** 9), 6))