n = int(input())
test = input()
res = 0

for i in range(0, n, n // 10):
    if not test[i:i + n // 10].count('N'):
        res += 1
print(res)

