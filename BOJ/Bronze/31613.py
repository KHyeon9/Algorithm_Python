x = int(input())
n = int(input())
res = 0
while x < n:
    res += 1
    if x % 3 == 0:
        x += 1
    elif x % 3 == 1:
        x *= 2
    elif x % 3 == 2:
        x *= 3

print(res)