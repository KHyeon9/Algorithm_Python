n = int(input())
nums = list(map(int, input().split()))
len_arr = []
now = 1

for i in range(1, n):
    # 오름차순인 경우 현제 길이 +=1
    if nums[i - 1] <= nums[i]:
        now += 1
    else:
        # 오름차순이 아닌 경우 배열에 길이 추가
        len_arr.append(now)
        # 길이 초기화
        now = 1
len_arr.append(now)
print(max(len_arr))
