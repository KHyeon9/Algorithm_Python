res = 0
for _ in range(int(input())):
    temp = max(list(map(int, input().split())))
    res += temp if temp > 0 else 0
print(res)