weight = [2, 7, 6, 5, 4, 3, 2]
dic = ['J', 'A', 'B', 'C', 'D', 'E', 'F',
       'G', 'H', 'I', 'Z']
nums = list(map(int, input()))
total = 0

for i in range(len(nums)):
    total += nums[i] * weight[i]
print(dic[total % 11])
