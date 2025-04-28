n = int(input())

# 점수 얻는 숫자들 저장
jackpot = {}
for _ in range(n):
    c, w = map(int, input().split())
    jackpot[c] = w

# 결과 저장
res = 0

# 슬롯 돌리기
m = int(input())
for _ in range(m):
    num = int(input())
    # 숫자가 잭팟인 경우
    if num in jackpot:
        res += jackpot[num]
    res -= 10

print(res)
    