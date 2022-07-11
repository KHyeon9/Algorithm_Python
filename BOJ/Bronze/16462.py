from math import ceil, floor

nums = []
student = int(input())
for _ in range(student):
    n = input()
    num = ""
    for i in n:
        if i == '0' or i == '6':
            num += '9'
            continue
        num += i
    num = int(num)
    if num > 100:
        num = 100
    nums.append(num)
res = sum(nums) / student
print(ceil(res) if res - int(res) >= 0.5 else floor(res))