res, sum = 0, 0

for _ in range(int(input())):
    v = int(input())
    sum += v
    if sum > res:
        res = sum

print(res + 100)