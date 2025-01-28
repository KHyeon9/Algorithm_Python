res = 0

for i in range(int(input())):
    if i % 2 == 0:
        res += 3
    else:
        res -= 2

print(res)