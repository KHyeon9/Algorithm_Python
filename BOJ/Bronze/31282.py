n, m, k = map(int, input().split())
dog, bunny, cnt = 0, n, 0

while dog < bunny:
    dog += k
    bunny += m
    cnt += 1

print(cnt)