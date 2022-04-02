n, m, l = map(int, input().split())
ball_cnt = [0] * n
num, result = 0, 0
while ball_cnt[num] < m - 1:
    ball_cnt[num] += 1
    result += 1
    if ball_cnt[num] % 2 == 1:
        num = (num + l) % n
    else:
        num = (num - l) % n

print(result)
