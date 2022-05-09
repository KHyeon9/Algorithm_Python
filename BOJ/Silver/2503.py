from itertools import permutations
nums = list(permutations([str(i) for i in range(1, 10)], 3))
for _ in range(int(input())):
    baseball, st, ba = map(int, input().split())
    baseball = str(baseball)
    remove_cnt = 0
    for i in range(len(nums)):
        st_cnt, ba_cnt = 0, 0
        i -= remove_cnt
        for j in range(3):
            if baseball[j] in nums[i]:
                if baseball[j] == nums[i][j]:
                    st_cnt += 1
                else:
                    ba_cnt += 1
        if st != st_cnt or ba != ba_cnt:
            nums.remove(nums[i])
            remove_cnt += 1
print(len(nums))
