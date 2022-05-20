n, m = map(int, input().split())
li = list(map(int, input().split()))
left, right = 0, max(li) * m

while left <= right:
    mid = (left + right) // 2
    cnt = sum(mid // i for i in li)

    if cnt >= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)
