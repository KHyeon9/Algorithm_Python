from itertools import product

N, K = map(int, input().split())
nums = list(input().split())
N_len = len(str(N))
nums_c = []
for i in range(1, N_len + 1):
    temp = product(nums, repeat=i)
    for num in temp:
        n = int("".join(num))
        if n <= N:
            nums_c.append(n)
print(max(nums_c))




