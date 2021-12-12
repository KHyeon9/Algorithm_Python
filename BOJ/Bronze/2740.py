from sys import stdin
n, m = map(int, stdin.readline().split())
arr = []
arr2 = []
for _ in range(n):
    nums = list(map(int, stdin.readline().split()))
    arr.append(nums)
m, k = map(int, stdin.readline().split())
for _ in range(m):
    nums2 = list(map(int, stdin.readline().split()))
    arr2.append(nums2)
answer = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            answer[i][j] += arr[i][l] * arr2[l][j]
for i in answer:
    print(*i)
