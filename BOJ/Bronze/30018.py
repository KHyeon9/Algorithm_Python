n = int(input())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = 0

for i in range(n):
    res += abs(nums1[i] - nums2[i])

print(res // 2)