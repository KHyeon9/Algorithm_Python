n = int(input())
x = int(input())
res = n / (n - n * (x / 100)) - 1
print(round(res * 100, 7))