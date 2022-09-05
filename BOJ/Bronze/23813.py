num = input()
n = len(num)
res = 0
for _ in range(n):
    num = num[-1] + num[:-1]
    res += int(num)
print(res)