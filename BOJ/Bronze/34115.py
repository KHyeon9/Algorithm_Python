n = int(input())
cards = list(map(int, input().split()))
# 숫자 처음 등장 위치
first_pos = [-1] * (n + 1)
res = 0

for i in range(2 * n):
    k = cards[i]
    if first_pos[k] == -1:
        # 처음 숫자가 등장한 경우
        first_pos[k] = i
    else:
        # 숫자가 다시 등장한 경우
        gap = i - first_pos[k] - 1
        res = max(res, gap)
print(res)
