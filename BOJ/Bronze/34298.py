r, s, n = map(int, input().split())
orders = list(map(int, input().split()))
now = 0
# r이 0인 경우
if r == 0:
    print(0)
else:
    for i in range(n):
        now = (now + orders[i]) % s
        # 나머지가 같은 경우
        if now == r:
            print(i + 1)
            break
    else:
        print(-1)