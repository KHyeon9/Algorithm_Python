from bisect import bisect_left

t = int(input())

for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    for i in a:
        cnt += bisect_left(b, i)
    print(cnt)
