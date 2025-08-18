nums = list(map(int, input().split()))
diff = 0
# 매칭 수가 다를 경우의 수 세기
for i in range(2):
    if nums[i] != nums[-i - 1]:
        diff += 1
# 팰린드롬이 가능한 경우
if diff <= 1:
    print("JAH")
    # 1개의 숫자를 바꿔야 하는 경우
    if diff == 1:
        if nums[0] != nums[-1]:
            nums[-1] = nums[0]
        else:
            nums[-2] = nums[1]
    print(*nums)
else:
    print("EI")




