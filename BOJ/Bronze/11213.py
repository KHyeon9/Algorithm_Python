n = int(input())
dice = list(map(int, input().split()))
dice_cnt = [0] * (max(dice) + 1)

for num in dice:
    dice_cnt[num] += 1

# 큰 수부터 확인
for i in range(len(dice_cnt) - 1, 0, -1):
    if dice_cnt[i] == 1:
        # 중복이 없는 눈 값 i를 던진 사람 순서 출력
        print(dice.index(i) + 1)
        exit()

print("none")