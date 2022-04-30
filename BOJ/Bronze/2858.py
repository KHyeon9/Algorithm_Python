r, b = map(int, input().split())

Sum = r + b

for i in range(3, Sum):
    if Sum % i == 0 and (i - 2) * (Sum // i - 2) == b:
        print(Sum // i, i)
        break