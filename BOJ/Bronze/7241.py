from itertools import permutations
nums = list(map(int, input().split()))
n = int(input())
arr = []

for i in permutations(nums, 3):
    arr.append(int("".join(map(str, [*i]))))
arr.sort()
print(arr.index(n) + 1)

