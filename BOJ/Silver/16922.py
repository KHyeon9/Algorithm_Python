from itertools import combinations_with_replacement
n = int(input())
nums = [1, 5, 10, 50]
nums_p = list(combinations_with_replacement(nums, n))
sum_n = []
for i in nums_p:
    if sum(i) not in sum_n:
        sum_n.append(sum(i))
print(len(sum_n))
