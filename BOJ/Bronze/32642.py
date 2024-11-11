n = int(input())
weather = list(map(int, input().split()))
now, res = 0, 0

for el in weather:
    if el == 1:
        now += 1
    else:
        now -= 1

    res += now

print(res)