from math import ceil
n, k = map(int, input().split())
arr = [[0, 0] for _ in range(6)]
answer = 0
for i in range(n):
    s, y = map(int, input().split())
    arr[y - 1][s - 1] += 1
for i in arr:
    answer += ceil(i[0] / k) + ceil(i[1] / k)
print(answer)
