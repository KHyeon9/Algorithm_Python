import sys
input = sys.stdin.readline

n, m = map(int, input().split())
IF = [input().split() for _ in range(n)]
for _ in range(m):
    num = int(input())
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if int(IF[mid][1]) >= num:
            right = mid
        else:
            left = mid + 1
    print(IF[right][0])