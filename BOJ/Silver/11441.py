from sys import stdin
input = stdin.readline()
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
temp = [0]
for i in range(n):
    temp.append(temp[i] + nums[i])

for _ in range(m):
    a, b = map(int, input().split())
    print(temp[b] - temp[a - 1])