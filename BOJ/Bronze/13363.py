n1 = int(input())
n2 = int(input())
res = n2 - n1

if res > 180:
    res -= 360
elif res <= -180:
    res += 360

print(res)
