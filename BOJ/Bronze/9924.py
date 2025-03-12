a, b = map(int, input().split())
cnt = 0

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
    cnt += 1
print(cnt)