money = [150, 30, 15, 5, 1]
res = [0] * 5

n = int(input())

for i in range(5):
    res[i] = n // money[i]
    n = n % money[i]

print(*res[::-1])